"""Compile and execute host adaptations of all 88 independent AVR solutions.

Only vendor syntax and hardware ADC conversion are adapted. These checks execute
real initialization, button filtering, timer/interrupt handlers and display code;
they do not establish native CodeVision compilation or physical timing.
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import tempfile
from zipfile import ZipFile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ROWS = json.loads((ROOT / 'problems.json').read_text())

Q1 = {
    'chase_fast': '''assert(value==7 && period_ms==100);
advance_time(99);assert(value==7);advance_time(1);assert(value==6);
for(i=0;i<50;i++)handle_buttons(1);assert(period_ms==10);
for(i=0;i<50;i++)handle_buttons(2);assert(period_ms==250);
value=0;advance_time(250);assert(value==7);render_display();assert(PORTD==0x7F);''',
    'chase_slow': '''assert(value==0);advance_time(100);assert(value==1);
for(i=0;i<50;i++)handle_buttons(1);assert(period_ms==40);
for(i=0;i<50;i++)handle_buttons(2);assert(period_ms==200);
value=7;advance_time(200);assert(value==0);''',
    'keypad10': '''assert(value==0);
for(i=0;i<1024;i++){set_keys(i);run(20);wanted=value;
if(i){wanted=0;for(j=0;j<10;j++)if(i&(1U<<j))wanted=j;}
assert(value==wanted);assert(PORTC==segments[wanted]);}
set_keys(0);run(20);assert(value==9);''',
    'keypad9': '''assert(value==0);
for(i=0;i<512;i++){set_keys(i);run(20);wanted=0;
for(j=0;j<9;j++)if(i&(1U<<j))wanted=j+1;
assert(value==wanted && PORTC==segments[wanted]);}
set_keys(0);run(20);assert(value==0);''',
    'single_wrap': '''assert(value==5);set_keys(1);run(650);assert(value==6);
set_keys(0);run(20);set_keys(1);run(20);assert(value==7);
value=9;handle_buttons(1);assert(value==0);handle_buttons(2);assert(value==9);''',
    'single_repeat': '''assert(value==5);set_keys(1);run(650);assert(value==8);
value=9;handle_buttons(1);assert(value==0);handle_buttons(2);assert(value==9);''',
    'single_clamp': '''assert(value==6);set_keys(1);run(650);assert(value==7);
for(i=0;i<30;i++)handle_buttons(1);assert(value==9);
for(i=0;i<30;i++)handle_buttons(2);assert(value==0);''',
    'single_auto_inc': '''assert(value==0 && !running);handle_buttons(1);
advance_time(99);assert(value==0);advance_time(1);assert(value==1);
value=9;advance_time(100);assert(value==0);
handle_buttons(2);advance_time(1000);assert(value==0 && !running);''',
    'single_auto_dec': '''assert(value==9 && !running);handle_buttons(1);
advance_time(299);assert(value==9);advance_time(1);assert(value==8);
value=0;advance_time(300);assert(value==9);
handle_buttons(2);advance_time(1000);assert(value==9 && !running);''',
    'single_period': '''assert(value==0 && running && period_ms==1000);
advance_time(999);assert(value==0);advance_time(1);assert(value==1);
for(i=0;i<50;i++)handle_buttons(1);assert(period_ms==2000);
for(i=0;i<50;i++)handle_buttons(2);assert(period_ms==200);
value=9;elapsed_ms=0;advance_time(200);assert(value==0);''',
    'toggle8_repeat': '''assert(value==0 && PORTD==255);
set_keys(0xA5);run(20);assert(value==0xA5 && PORTD==0x5A);
run(299);assert(value==0xA5);run(1);assert(value==0);
set_keys(0);run(20);set_keys(0x42);run(20);assert(value==0x42);''',
    'toggle8': '''assert(value==0);set_keys(0xA5);run(650);assert(value==0xA5);
set_keys(0);run(20);set_keys(0x42);run(20);assert(value==0xE7);''',
    'shift_buttons': '''assert(value==6);set_keys(1);run(420);assert(value==3);
value=0;handle_buttons(1);assert(value==7);handle_buttons(2);assert(value==0);
render_display();assert(PORTD==254);''',
    'blink': '''assert(period_ms==50 && value==0xAA);
advance_time(49);assert(value==0xAA);advance_time(1);assert(value==0x55);
advance_time(50);assert(value==0xAA);
for(i=0;i<500;i++)handle_buttons(1);assert(period_ms==5);
for(i=0;i<500;i++)handle_buttons(2);assert(period_ms==1000);''',
}
Q2 = {
    'timer_ext_limits': '''assert(value==8000 && MCUCR==10 && GICR==192);
for(i=0;i<1000;i++)ext_int0_isr();assert(value==8888);
for(i=0;i<1000;i++)ext_int1_isr();assert(value==8000);
handle_buttons(1);value=9000;elapsed_ms=0;
for(i=0;i<249;i++){TCNT0=0;timer0_overflow();}assert(value==9000);
TCNT0=0;timer0_overflow();assert(value==1000 && TCNT0==6);
ext_int0_isr();assert(value==8000);
handle_buttons(2);advance_time(1000);assert(value==8000 && !running);''',
    'timer_auto_inc': '''assert(value==1234 && TCCR0==3 && TCCR2==4);
value=9999;handle_buttons(1);assert(value==9999);
value=0;handle_buttons(2);assert(value==0);
value=9998;handle_buttons(4);elapsed_ms=0;
for(i=0;i<249;i++){TCNT0=0;timer0_overflow();}assert(value==9998);
TCNT0=0;timer0_overflow();assert(value==9999 && !running);
advance_time(500);assert(value==9999);''',
    'timer_auto_dec': '''assert(value==1234 && TCCR0==4 && TCCR2==4);
value=9999;handle_buttons(1);assert(value==9999);
value=0;handle_buttons(2);assert(value==0);
value=1;handle_buttons(4);elapsed_ms=0;
for(i=0;i<124;i++){TCNT0=0;timer0_overflow();}assert(value==1);
TCNT0=0;timer0_overflow();assert(value==0 && !running && TCNT0==131);
advance_time(500);assert(value==0);''',
    'timer_start': '''assert(value==1111 && TCCR0==4 && MCUCR==2);
value=9000;handle_buttons(1);assert(value==9000);
value=1000;handle_buttons(2);assert(value==1000);
value=9000;handle_buttons(4);elapsed_ms=0;
for(i=0;i<124;i++){TCNT0=0;timer0_overflow();}assert(value==9000);
TCNT0=0;timer0_overflow();assert(value==1000);
ext_int0_isr();advance_time(500);assert(value==1000 && !running);''',
    'reset1000': '''assert(value==1000 && MCUCR==2 && GICR==64);
set_keys(1);run(650);assert(value==1001);
value=9999;handle_buttons(1);assert(value==9999);
value=0;handle_buttons(2);assert(value==0);
ext_int0_isr();assert(value==1000);''',
    'count6000': '''assert(value==6000 && MCUCR==12 && GICR==128);
handle_buttons(1);advance_time(999);assert(value==6000);
advance_time(1);assert(value==5999);
value=1;elapsed_ms=0;advance_time(1000);assert(value==0 && !running);
ext_int1_isr();assert(value==6000);
handle_buttons(1);handle_buttons(2);advance_time(1000);assert(value==6000);''',
    'auto_period_inc': '''assert(value==0 && !running && MCUCR==8);
ext_int1_isr();advance_time(1000);assert(value==1);
for(i=0;i<50;i++)handle_buttons(1);assert(period_ms==2000);
for(i=0;i<50;i++)handle_buttons(2);assert(period_ms==100);
value=9000;elapsed_ms=0;advance_time(100);assert(value==0);''',
    'auto_period_dec': '''assert(value==0 && !running && MCUCR==10);
ext_int0_isr();advance_time(1000);assert(value==9999);
ext_int1_isr();advance_time(1000);assert(value==9999 && !running);
for(i=0;i<50;i++)handle_buttons(1);assert(period_ms==2000);
for(i=0;i<50;i++)handle_buttons(2);assert(period_ms==100);''',
    'toggle_period': '''assert(value==5555 && !running && MCUCR==10);
set_keys(1);run(650);assert(running);set_keys(0);run(20);
set_keys(1);run(20);assert(!running);
for(i=0;i<50;i++)ext_int0_isr();assert(period_ms==3000);
for(i=0;i<50;i++)ext_int1_isr();assert(period_ms==500);
handle_buttons(1);value=9999;elapsed_ms=0;advance_time(500);assert(value==0);''',
    'countdown10': '''assert(value==10 && MCUCR==2);
set_keys(1);run(420);assert(value==13);
value=9999;handle_buttons(1);assert(value==9999);
value=1;handle_buttons(2);assert(value==1);
ext_int0_isr();advance_time(999);assert(value==1);
advance_time(1);assert(value==10 && !running);''',
    'adc_precision': '''assert(precision==0 && channel==0);
for(j=0;j<2;j++){for(i=0;i<1024;i++){adc_samples[0]=i;tick_1ms();
assert(value==(i*(j?500UL:50UL)+511)/1023);
assert(display_dp==(j?2:4));assert(PORTB==segments[j+1]);}
handle_buttons(1);}
assert(precision==0);''',
    'adc_channel_button': '''assert(channel==0);
set_keys(1);run(650);assert(channel==1);
set_keys(0);run(20);set_keys(1);run(20);assert(channel==2);
set_keys(0);run(20);set_keys(1);run(20);assert(channel==0);
for(j=0;j<3;j++){channel=j;for(i=0;i<1024;i++){
adc_samples[j]=i;tick_1ms();assert(value==(i*50UL+511)/1023);
assert(PORTB==segments[j] && display_dp==4);}}''',
    'adc_channel_irq': '''assert(channel==0 && MCUCR==12 && GICR==128);
ext_int1_isr();assert(channel==1);ext_int1_isr();assert(channel==2);
ext_int1_isr();assert(channel==0);
for(j=0;j<3;j++){channel=j;for(i=0;i<1024;i++){
adc_samples[j]=i;tick_1ms();assert(value==(i*50UL+511)/1023);
assert(PORTB==segments[j]);}}''',
    'adc_lm35': '''assert(!temperature_mode && !precision);
for(j=0;j<2;j++){for(i=0;i<1024;i++){adc_samples[0]=i;tick_1ms();
assert(value==(i*(j?500UL:50UL)+511)/1023);
assert(display_dp==(j?1:2));assert(PORTB==(j?9:5));}
handle_buttons(2);}
handle_buttons(1);assert(temperature_mode);
for(i=0;i<1024;i++){adc_samples[1]=i;tick_1ms();
assert(value==(i*500UL+511)/1023 && !display_dp && PORTB==2);}
adc_samples[1]=51;tick_1ms();assert(value==25);
handle_buttons(1);assert(!temperature_mode);''',
}


def pin_setter(kind, question):
    if question == 1:
        if kind.startswith('chase_'):
            return 'PINC=(unsigned char)~mask;'
        if kind == 'shift_buttons':
            return 'PINA=(unsigned char)~(mask<<1);'
        if kind == 'blink':
            return 'PINB=(unsigned char)~(mask<<6);'
        if kind in ('keypad9', 'keypad10'):
            return 'PINA=(unsigned char)~mask;PINB=(unsigned char)~(mask>>8);'
        return 'PINA=(unsigned char)~mask;'
    if kind == 'reset1000':
        return 'PIND=(unsigned char)~(mask<<6);'
    if kind.startswith('adc_'):
        return 'PIND=(unsigned char)~mask;'
    if kind in ('toggle_period', 'auto_period_inc', 'countdown10'):
        return 'PINA=(unsigned char)~mask;'
    return 'PINB=(unsigned char)~mask;'


def run_checked(command):
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        raise AssertionError(f'{command[0]} exited {result.returncode}\n{result.stdout}{result.stderr}')


def main():
    assert len(ROWS) == 44 and [r['set'] for r in ROWS] == list(range(1, 45))
    with ZipFile(ROOT / 'DC2DT29 de cuong.docx') as document:
        xml = ET.fromstring(document.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    original = '\n'.join(''.join(t.text or '' for t in p.findall('.//w:t', ns))
                         for p in xml.findall('.//w:p', ns))
    sets = re.split(r'Câu 1\s*\(4 điểm\)', original)[1:]
    assert len(sets) == 44
    normalize = lambda text: ''.join(c.lower() for c in text if c.isalnum())
    for text, row in zip(sets, ROWS):
        questions = re.split(r'Câu 2\s*\(6 điểm\)', text)
        assert len(questions) == 2
        for q, wording in enumerate(questions, 1):
            assert normalize(wording) == normalize(row[f'q{q}']), (row['set'], q)
    expected = {ROOT / f"de_{r['set']:02d}" / f'cau_{q}.c' for r in ROWS for q in (1, 2)}
    actual = set(ROOT.glob('de_*/cau_*.c'))
    assert actual == expected, f'Expected all 88 solutions; missing {len(expected-actual)}, extra {len(actual-expected)}'
    gcc = shutil.which('gcc')
    assert gcc, 'GCC must be on PATH'
    registers = 'PORTA PORTB PORTC PORTD DDRA DDRB DDRC DDRD PINA PINB PINC PIND SREG TCCR0 TCNT0 TCCR2 TCNT2 TIMSK MCUCR MCUCSR GICR GIFR ADMUX ADCSRA'.split()
    with tempfile.TemporaryDirectory(prefix='dc2dt29_') as tmp:
        tmp = Path(tmp)
        for row in ROWS:
            for q in (1, 2):
                path = ROOT / f"de_{row['set']:02d}" / f'cau_{q}.c'
                code = path.read_text()
                kind = row[f'q{q}_kind']
                code = re.sub(r'^#include <(?:mega16|delay)\.h>\s*$', '', code, flags=re.M)
                code = re.sub(r'interrupt \[[^\]]+\]\s*', '', code)
                code = re.sub(r'#asm\("(?:cli|sei)"\)', '', code)
                code = code.replace('void main(void)', 'void firmware(void)')
                # Replace only the peripheral conversion; all scaling remains real.
                if kind.startswith('adc_'):
                    code, n = re.subn(r'unsigned int read_adc\(unsigned char input\)\s*\{.*?\n\}',
                        'unsigned int read_adc(unsigned char input) { return adc_samples[input]; }', code, flags=re.S)
                    assert n == 1
                prelude = '#include <assert.h>\n#include <stdio.h>\n'
                prelude += '\n'.join(f'unsigned char {r}={255 if r.startswith("PIN") else 0};' for r in registers)
                prelude += '\nunsigned int ADCW,adc_samples[3];\nvoid delay_ms(unsigned int ms){(void)ms;}\nvoid delay_us(unsigned int us){(void)us;}\n'
                timer_ms = 4 if kind in ('timer_auto_dec', 'timer_start') else 2
                run = f'''void set_keys(unsigned int mask){{{pin_setter(kind,q)}}}
void run(unsigned int ms){{while(ms--){{tick_1ms();''' + (
                    f'if(++timer_phase=={timer_ms}){{timer_phase=0;TCNT0=0;timer0_overflow();}}' if kind.startswith('timer_') else ''
                ) + '}}\n'
                checks = (Q1 if q == 1 else Q2)[kind]
                extras = ''
                if kind in ('timer_auto_inc', 'timer_auto_dec'):
                    extras += '''value=1234;render_display();scan_index=0;
for(i=0;i<4;i++){TCNT2=0;timer2_overflow();assert(TCNT2==6);
assert((PORTA&0xF0)==(1U<<(i+4)));assert(PORTC==segments[i+1]);}
assert((TIMSK&0x41)==0x41);'''
                if q == 1 and kind in ('chase_fast', 'chase_slow'):
                    repeats = kind == 'chase_slow' or row['set'] != 1
                    extras += f'''initialize();set_keys(1);run(420);
assert(period_ms=={70 if repeats else 90});'''
                if kind == 'timer_start':
                    extras += f'''initialize();set_keys(1);run(650);assert(value=={1112 if row['set']==3 else 1115});'''
                if q == 1 and kind == 'chase_fast' and row['set'] != 1:
                    extras += '''initialize();period_ms=250;set_keys(2);run(1020);assert(value==3);'''
                if kind == 'single_period':
                    extras += '''initialize();period_ms=2000;set_keys(1);run(2020);assert(value==1);'''
                if kind == 'auto_period_inc':
                    extras += '''initialize();period_ms=2000;ext_int1_isr();set_keys(1);run(2020);assert(value==1);'''
                if kind == 'auto_period_dec':
                    extras += '''initialize();period_ms=2000;ext_int0_isr();set_keys(1);run(2020);assert(value==9999);'''
                if kind == 'chase_slow':
                    extras += '''initialize();period_ms=200;set_keys(2);run(1020);assert(value==5);'''
                if kind == 'blink':
                    extras += '''initialize();period_ms=1000;set_keys(2);run(1020);assert(value==0x55);'''
                if kind == 'timer_start':
                    extras += '''initialize();timer_phase=0;set_keys(4);run(1020);assert(value==1113);'''
                debounce = '''wanted=value;set_keys(1);run(10);set_keys(0);run(20);
assert(value==wanted);initialize();'''
                gpio = ('assert(DDRA==0xF0 && DDRC==255);' if q == 2 else
                        'assert(DDRD==255);' if kind in ('chase_fast','chase_slow','blink','shift_buttons','toggle8','toggle8_repeat') else
                        'assert(DDRC==255);')
                harness = prelude + '\n' + code + '\nunsigned int timer_phase;\n' + run + f'''
int main(void){{unsigned int i,j,wanted;(void)i;(void)j;(void)wanted;
MCUCSR=0x5A;initialize();assert(MCUCSR==0x5A);
{gpio}
{debounce}
{checks}
{extras}
assert(MCUCSR==0x5A);puts("PASS");return 0;}}
'''
                c = tmp / 'check.c'
                exe = tmp / 'check'
                c.write_text(harness.replace(';assert', ';\nassert'))
                run_checked([gcc, '-std=c99', '-Wall', '-Wextra', '-Werror', '-O1', '-fsanitize=undefined', '-fno-sanitize-recover=all', str(c), '-o', str(exe)])
                run_checked([str(exe)])
                print(f"PASS de_{row['set']:02d}/cau_{q}.c ({kind})", flush=True)
    print('PASS 88/88 host adaptations. Not a native CodeVisionAVR build or Proteus simulation.')


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Run tests without Python -O: assertions must remain enabled')
    main()
