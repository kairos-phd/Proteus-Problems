"""Host checks of real main-loop code; not a native CodeVisionAVR/Proteus build."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ROWS = json.loads((ROOT / 'problems.json').read_text())

AVR_BITS = {'ACBG': 6,
 'ACD': 7,
 'ACI': 4,
 'ACIC': 2,
 'ACIE': 3,
 'ACIS0': 0,
 'ACIS1': 1,
 'ACME': 3,
 'ACO': 5,
 'ADATE': 5,
 'ADEN': 7,
 'ADIE': 3,
 'ADIF': 4,
 'ADLAR': 5,
 'ADPS0': 0,
 'ADPS1': 1,
 'ADPS2': 2,
 'ADSC': 6,
 'AS2': 3,
 'COM00': 4,
 'COM01': 5,
 'COM1A0': 6,
 'COM1A1': 7,
 'COM1B0': 4,
 'COM1B1': 5,
 'COM20': 4,
 'COM21': 5,
 'CPHA': 2,
 'CPOL': 3,
 'CS00': 0,
 'CS01': 1,
 'CS02': 2,
 'CS10': 0,
 'CS11': 1,
 'CS12': 2,
 'CS20': 0,
 'CS21': 1,
 'CS22': 2,
 'CTC2': 3,
 'DORD': 5,
 'ICES1': 6,
 'ICNC1': 7,
 'INT0': 6,
 'INT1': 7,
 'INT2': 5,
 'INTF0': 6,
 'INTF1': 7,
 'INTF2': 5,
 'ISC00': 0,
 'ISC01': 1,
 'ISC10': 2,
 'ISC11': 3,
 'MSTR': 4,
 'MUX0': 0,
 'MUX1': 1,
 'MUX2': 2,
 'MUX3': 3,
 'MUX4': 4,
 'OCIE0': 1,
 'OCIE1A': 4,
 'OCIE1B': 3,
 'OCIE2': 7,
 'PWM2': 6,
 'REFS0': 6,
 'REFS1': 7,
 'RXB8': 1,
 'RXCIE': 7,
 'RXEN': 4,
 'SPE': 6,
 'SPIE': 7,
 'SPR0': 0,
 'SPR1': 1,
 'TICIE1': 5,
 'TOIE0': 0,
 'TOIE1': 2,
 'TOIE2': 6,
 'TWEA': 6,
 'TWEN': 2,
 'TWIE': 0,
 'TWSTA': 5,
 'TWSTO': 4,
 'TXB8': 0,
 'TXCIE': 6,
 'TXEN': 3,
 'UCSZ2': 2,
 'UDRIE': 5,
 'WGM00': 6,
 'WGM01': 3,
 'WGM10': 0,
 'WGM11': 1,
 'WGM12': 3,
 'WGM13': 4}
for port in 'ABCD':
    for bit in range(8):
        AVR_BITS[f'DD{port}{bit}'] = bit
        AVR_BITS[f'PORT{port}{bit}'] = bit

Q1 = {
'chase_fast': '''assert(PORTD==0x7F);run(99);assert(PORTD==0x7F);run(1);assert(PORTD==0xBF);
keys(1);run(420);assert(t==HOLD_PERIOD);keys(0);step();
for(i=0;i<50;i++){press(1);}assert(t==10);
for(i=0;i<50;i++){press(2);}assert(t==250);
old=PORTD;keys(2);run(1000);assert(PORTD!=old);''',
'chase_slow': '''assert(PORTD==0xFE);run(100);assert(PORTD==0xFD);
keys(1);run(420);assert(t==70);keys(0);step();
for(i=0;i<50;i++){press(1);}assert(t==40);
for(i=0;i<50;i++){press(2);}assert(t==200);''',
'shift_buttons': '''assert(PORTD==0xBF);keys(1);run(420);assert(PORTD==0xF7);
keys(0);step();led=1;press(1);assert(PORTD==0x7F);press(2);assert(PORTD==0xFE);''',
'blink': '''assert(PORTD==0xAA);run(49);assert(PORTD==0xAA);run(1);assert(PORTD==0x55);
run(50);assert(PORTD==0xAA);for(i=0;i<500;i++){press(1);}assert(t==5);
for(i=0;i<500;i++){press(2);}assert(t==1000);
keys(2);run(1000);assert(PORTD==0xAA || PORTD==0x55);''',
'keypad10': '''for(i=0;i<1024;i++){keys(i);step();want=so;
if(i){want=0;for(j=0;j<10;j++)if(i&(1U<<j))want=j;}
assert(so==want && PORTC==codes[want]);}keys(0);step();assert(so==9);''',
'keypad9': '''for(i=0;i<512;i++){keys(i);step();want=0;
for(j=0;j<9;j++)if(i&(1U<<j))want=j+1;
assert(so==want && PORTC==codes[want]);}keys(0);step();assert(so==0);''',
'single_wrap': '''assert(so==5);keys(1);run(650);assert(so==6);
keys(0);step();so=9;press(1);assert(so==0);press(2);assert(so==9);''',
'single_repeat': '''assert(so==5);keys(1);run(650);assert(so==8);
keys(0);step();so=9;press(1);assert(so==0);press(2);assert(so==9);''',
'single_clamp': '''assert(so==6);keys(1);run(650);assert(so==7);keys(0);step();
for(i=0;i<30;i++){press(1);}assert(so==9);
for(i=0;i<30;i++){press(2);}assert(so==0);''',
'single_auto_inc': '''assert(so==0 && !chay);press(1);dem=0;
run(90);assert(so==0);run(10);assert(so==1);
so=9;dem=0;run(100);assert(so==0);press(2);old=so;run(1000);assert(so==old && !chay);''',
'single_auto_dec': '''assert(so==9 && !chay);press(1);dem=0;
run(290);assert(so==9);run(10);assert(so==8);
so=0;dem=0;run(300);assert(so==9);press(2);old=so;run(1000);assert(so==old && !chay);''',
'single_period': '''assert(so==0 && t==1000);run(999);assert(so==0);run(1);assert(so==1);
for(i=0;i<50;i++){press(1);}assert(t==2000);
for(i=0;i<50;i++){press(2);}assert(t==200);
so=9;dem=0;run(200);assert(so==0);''',
 'toggle8': '''assert(PORTD==255);keys(0xA5);run(650);assert(PORTD==0x5A);
keys(0);step();keys(0x42);step();assert(PORTD==0x18);''',
 'toggle8_repeat': '''assert(PORTD==255);keys(0xA5);run(300);assert(PORTD==0x5A);
run(1);assert(PORTD==255);keys(0);step();keys(0x42);step();assert(PORTD==0xBD);''',
}
Q2 = {
 'timer_ext_limits': '''assert(so==8000 && MCUCR==10 && GICR==192);
for(i=0;i<1000;i++){ext_int0_isr();}assert(so==8888);
for(i=0;i<1000;i++){ext_int1_isr();}assert(so==8000);
press(1);so=9000;dem=0;for(i=0;i<249;i++){TCNT0=0;timer0_overflow();}assert(so==9000);
TCNT0=0;timer0_overflow();assert(so==1000 && TCNT0==6);ext_int0_isr();assert(so==8000);
press(2);old=so;run(1000);assert(so==old && !chay);''',
 'timer_auto_inc': '''assert(so==1234 && TCCR0==3 && TCCR2==4);run(8);assert(shown()==1234);
so=9999;press(1);assert(so==9999);so=0;press(2);assert(so==0);
so=9998;press(4);dem=0;for(i=0;i<249;i++){TCNT0=0;timer0_overflow();}assert(so==9998);
TCNT0=0;timer0_overflow();assert(so==9999 && !chay);run(500);assert(so==9999);''',
 'timer_auto_dec': '''assert(so==1234 && TCCR0==4 && TCCR2==4);run(8);assert(shown()==1234);
so=9999;press(1);assert(so==9999);so=0;press(2);assert(so==0);
so=1;press(4);dem=0;for(i=0;i<124;i++){TCNT0=0;timer0_overflow();}assert(so==1);
TCNT0=0;timer0_overflow();assert(so==0 && !chay && TCNT0==131);''',
 'timer_start': '''assert(so==1111 && TCCR0==4 && MCUCR==2);
keys(1);run(650);assert(so==MANUAL_VALUE);keys(0);step();
so=9000;press(1);assert(so==9000);so=1000;press(2);assert(so==1000);
so=9000;press(4);dem=0;for(i=0;i<125;i++){TCNT0=0;timer0_overflow();}assert(so==1000);
ext_int0_isr();run(500);assert(so==1000 && !chay);
so=1111;dem=0;keys(4);run(1020);assert(so==1113);''',
 'reset1000': '''assert(so==1000 && MCUCR==2);keys(1);run(650);assert(so==1001);
keys(0);step();so=9999;press(1);assert(so==9999);so=0;press(2);assert(so==0);
ext_int0_isr();assert(so==1000);''',
 'count6000': '''assert(so==6000 && MCUCR==12);press(1);dem=0;
run(999);assert(so==6000);run(1);assert(so==5999);
so=1;dem=0;run(1000);assert(so==0 && !chay);ext_int1_isr();assert(so==6000);
press(1);press(2);run(1000);assert(so==6000);''',
 'auto_period_inc': '''assert(so==0 && !chay && MCUCR==8);ext_int1_isr();run(1000);assert(so==1);
for(i=0;i<50;i++){press(1);}assert(t==2000);
for(i=0;i<50;i++){press(2);}assert(t==100);
so=9000;dem=0;run(100);assert(so==0);''',
 'auto_period_dec': '''assert(so==0 && !chay && MCUCR==10);ext_int0_isr();run(1000);assert(so==9999);
ext_int1_isr();run(1000);assert(so==9999 && !chay);
for(i=0;i<50;i++){press(1);}assert(t==2000);
for(i=0;i<50;i++){press(2);}assert(t==100);''',
 'toggle_period': '''assert(so==5555 && !chay);keys(1);run(650);assert(chay);
keys(0);step();press(1);assert(!chay);
for(i=0;i<50;i++){ext_int0_isr();}assert(t==3000);
for(i=0;i<50;i++){ext_int1_isr();}assert(t==500);
press(1);so=9999;dem=0;run(500);assert(so==0);''',
 'countdown10': '''assert(so==10 && MCUCR==2);keys(1);run(420);assert(so==13);
keys(0);step();so=9999;press(1);assert(so==9999);so=1;press(2);assert(so==1);
ext_int0_isr();run(999);assert(so==1);run(1);assert(so==10 && !chay);''',
 'adc_precision': '''assert(le==1);for(j=1;j<=2;j++){
for(i=0;i<1024;i++){adc_samples[0]=i;run(4);assert(so==(i*(j==1?50UL:500UL)+511)/1023);
assert(shown()==so && dp==(j==1?4:2) && PORTB==codes[j]);}press(1);}assert(le==1);''',
 'adc_channel_button': '''assert(kenh==0);keys(1);run(650);assert(kenh==1);
keys(0);step();press(1);assert(kenh==2);press(1);assert(kenh==0);
for(j=0;j<3;j++){kenh=j;for(i=0;i<1024;i++){adc_samples[j]=i;run(4);
assert(so==(i*50UL+511)/1023 && shown()==so && PORTB==codes[j] && dp==4);}}''',
 'adc_channel_irq': '''assert(kenh==0 && MCUCR==12);ext_int1_isr();assert(kenh==1);
ext_int1_isr();assert(kenh==2);ext_int1_isr();assert(kenh==0);
for(j=0;j<3;j++){kenh=j;for(i=0;i<1024;i++){adc_samples[j]=i;run(4);
assert(so==(i*50UL+511)/1023 && shown()==so && PORTB==codes[j] && dp==4);}}''',
 'adc_lm35': '''assert(chedo==0 && le==1);
for(j=1;j<=2;j++){for(i=0;i<1024;i++){adc_samples[0]=i;run(3);
assert(so==(i*(j==1?50UL:500UL)+511)/1023 && shown()==so);
assert(dp==(j==1?2:1) && PORTB==(j==1?5:9));}press(2);}
press(1);for(i=0;i<1024;i++){adc_samples[1]=i;run(3);
assert(so==(i*500UL+511)/1023 && shown()==so && dp==0 && PORTB==2);}
adc_samples[1]=51;run(3);assert(so==25);''',
}


def pin_setter(kind, question):
    if question == 1:
        if kind.startswith('chase'):return 'PINC=(unsigned char)~mask;'
        if kind == 'shift_buttons':return 'PINA=(unsigned char)~(mask<<1);'
        if kind == 'blink':return 'PINB=(unsigned char)~(mask<<6);'
        if kind.startswith('keypad'):return 'PINA=(unsigned char)~mask;PINB=(unsigned char)~(mask>>8);'
        return 'PINA=(unsigned char)~mask;'
    if kind == 'reset1000':return 'PIND=(unsigned char)~(mask<<6);'
    if kind.startswith('adc_'):return 'PIND=(unsigned char)~mask;'
    if kind in ('auto_period_inc','toggle_period','countdown10'):return 'PINA=(unsigned char)~mask;'
    return 'PINB=(unsigned char)~mask;'


def checked(command, label):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise AssertionError(f'{label}: {result.returncode}\n{result.stdout}{result.stderr}')


def main():
    expected = {ROOT/f"de_{r['set']:02d}"/f'cau_{q}.c' for r in ROWS for q in (1,2)}
    assert len(expected)==88 and set(ROOT.glob('de_*/cau_*.c'))==expected
    gcc=shutil.which('gcc')
    assert gcc, 'GCC must be available'
    registers='PORTA PORTB PORTC PORTD DDRA DDRB DDRC DDRD PINA PINB PINC PIND SREG TCCR0 TCNT0 OCR0 TCCR1A TCCR1B TCNT1H TCNT1L ICR1H ICR1L OCR1AH OCR1AL OCR1BH OCR1BL ASSR TCCR2 TCNT2 OCR2 TIMSK MCUCR MCUCSR GICR GIFR UCSRB ACSR SFIOR ADMUX ADCSRA SPCR TWCR'.split()
    prelude='#include <assert.h>\n#include <stdio.h>\n'
    prelude+='\n'.join(f'#define {k} {v}' for k,v in AVR_BITS.items())+'\n'
    prelude+='\n'.join(f'unsigned char {r}={255 if r.startswith("PIN") else 0};' for r in registers)
    prelude+='\nunsigned int ADCW,adc_samples[3];\nunsigned long elapsed_delay,last_delay;\nvoid delay_ms(unsigned int n){elapsed_delay+=n;}\nvoid delay_us(unsigned int n){(void)n;}\nvoid host_release(unsigned char *pin,unsigned char bit){*pin|=1U<<bit;}\n'
    prelude+='unsigned char codes[10]={0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90};\n'
    header=(ROOT.parent/'bai_06.c').read_text().split('#include',1)[0].replace('8/24/2026','10/21/2026')
    header_lines=[line.strip() for line in header.splitlines() if line.strip()]
    with tempfile.TemporaryDirectory(prefix='avr_direct_') as folder:
        folder=Path(folder)
        for row in ROWS:
            for q in (1,2):
                path=ROOT/f"de_{row['set']:02d}"/f'cau_{q}.c'
                text=path.read_text();kind=row[f'q{q}_kind']
                assert [line.strip() for line in text.split('#include',1)[0].splitlines() if line.strip()]==header_lines, path
                assert not any(f' {f}(' in text for f in ('docnut','xulynut','demthoigian')), path
                globals_text,main_text=text.split('void main(void)\n{\n',1)
                locals_text,setup=main_text.split('    // Input/Output Ports initialization',1)
                setup,loop=setup.split('while (1)\n{\n',1)
                loop=loop.rsplit('\n}\n}',1)[0]
                source=globals_text+locals_text+'\nvoid initialize(void){\n'+setup+'\n}\nvoid step_code(void){\n'+loop+'\n}\n'
                source=re.sub(r'^#include <(?:mega16|delay)\.h>\s*$', '',source,flags=re.M)
                source=re.sub(r'#asm\("(?:cli|sei)"\)', '',source)
                source=re.sub(r'interrupt \[[^\]]+\] ', '',source)
                # Emulate the physical release that ends a standalone button wait.
                source=re.sub(r'while\s*\(\s*(PIN[A-D])\.([0-7])\s*==\s*0\s*\)\s*;', r'host_release(&\1,\2);', source)
                source=re.sub(r'\b(PIN[A-D])\.([0-7])',r'((\1 >> \2) & 1)',source)
                if kind.startswith('adc_'):
                    source,n=re.subn(r'unsigned int docadc\(unsigned char kenh\)\n\{.*?\n\}',
                        'unsigned int docadc(unsigned char kenh){ADMUX=0x40|kenh;return adc_samples[kenh];}',source,flags=re.S)
                    assert n==1
                support='''unsigned int phase0,phase2;int displayed[4];unsigned char dp;
void observe(void){unsigned int k,d;for(k=0;k<DIGITS;k++)if(PORTA&(1U<<(k+4))){
displayed[k]=-1;for(d=0;d<10;d++)if((PORTC|0x80)==codes[d])displayed[k]=d;
if(PORTC&0x80)dp&=~(1U<<k);else dp|=1U<<k;}}
unsigned int shown(void){unsigned int k,n=0;for(k=0;k<DIGITS;k++){assert(displayed[k]>=0);n=n*10+displayed[k];}return n;}
void keys(unsigned int mask){PINA=PINB=PINC=PIND=255;PIN_SETTER}
void step(void){unsigned long before=elapsed_delay;step_code();last_delay=elapsed_delay-before;TIMER0 TIMER2 OBSERVE}
void run(unsigned int n){unsigned long spent=0;while(spent<n){step();spent+=last_delay?last_delay:1;}}
void press(unsigned int mask){keys(0);step();keys(mask);step();keys(0);step();}
'''
                tick=4 if kind in ('timer_start','timer_auto_dec') else 2
                support=support.replace('DIGITS',str(3 if kind=='adc_lm35' else 4))
                support=support.replace('PIN_SETTER',pin_setter(kind,q))
                support=support.replace('TIMER0',f'if(++phase0=={tick}){{phase0=0;TCNT0=0;timer0_overflow();}}' if kind.startswith('timer_') else '')
                support=support.replace('TIMER2','if(++phase2==2){phase2=0;TCNT2=0;timer2_overflow();}' if kind in ('timer_auto_inc','timer_auto_dec') else '')
                support=support.replace('OBSERVE','observe();' if q==2 else '')
                case=(Q1 if q==1 else Q2)[kind]
                case=case.replace('HOLD_PERIOD',str(90 if row['set']==1 else 70))
                case=case.replace('MANUAL_VALUE',str(1112 if row['set']==3 else 1115))
                harness=prelude+source+support+'\nint main(void){unsigned int i,j,want,old;(void)i;(void)j;(void)want;(void)old;\nMCUCSR=0x5A;initialize();\n'+case+'\nassert(MCUCSR==0x5A);puts("PASS");return 0;}\n'
                c=folder/'check.c';exe=folder/'check';c.write_text(harness.replace(';assert',';\nassert'))
                checked([gcc,'-std=c99','-Wall','-Wextra','-Werror','-O1','-fsanitize=undefined','-fno-sanitize-recover=all',str(c),'-o',str(exe)],str(path))
                checked([str(exe)],str(path))
                print(f"PASS de_{row['set']:02d}/cau_{q}.c",flush=True)
    print('PASS 88/88 direct-loop host checks. Native CodeVisionAVR and Proteus remain unverified.')


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Run without Python -O')
    main()
