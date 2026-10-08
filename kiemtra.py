from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
EXPECTED = set(range(1, 17)) | set(range(23, 32))
FILES = {int(p.stem.split('_')[1]): p for p in ROOT.glob('bai_*.c')}
assert set(FILES) == EXPECTED, 'Expected exactly 25 exercises, excluding 17-22'
GCC = shutil.which('gcc')
assert GCC, 'gcc must be installed and available on PATH'

TESTS = {
1: '''step(); PIND=0xFA; step(); assert(PORTC==0xFA);
PIND=255; step(); assert(PORTC==0xFA);
PIND=0xEF; step(); assert(PORTC==0xEA);''',
2: '''for(int v=0;v<256;v++){PIND=v;step();assert(PORTC==v);}''',
3: '''step(); PIND=0xFE;step();PIND=255;step();step();assert(PORTC==255);
PIND=0xFA;step();step();assert(PORTC==0xFA);
repeat(20);assert(PORTC==0xFA);
PIND=255;step();step();PIND=0xFA;step();step();assert(PORTC==255);''',
4: '''step();assert(elapsed==1000);assert(trace_count==2);
assert(trace_port[0]==0 && trace_ms[0]==500);
assert(trace_port[1]==255 && trace_ms[1]==500);''',
5: '''for(int k=0;k<16;k++){step();assert(PORTC==(unsigned char)~(0x80>>(k%8)));}
assert(elapsed==3200);''',
6: '''for(int k=0;k<21;k++){step();assert(PORTC==digits[k%10]);}
assert(elapsed==21000);''',
7: '''step();assert(PORTC==digits[0]);press(2);assert(PORTC==digits[9]);
repeat(20);assert(PORTC==digits[9]);release();press(1);assert(PORTC==digits[0]);
release();press(1);assert(PORTC==digits[1]);''',
8: '''for(int k=0;k<37;k++){int p=k%18;int want=p<=9?p:18-p;step();assert(PORTC==digits[want]);}
assert(elapsed==37000);''',
9: '''repeat(49);assert(dem==0 && elapsed==980);step();assert(dem==1 && elapsed==1000);
step();assert(shown()==1);assert(last_select_mask==0xF0);
dem=9999;dem_ms=980;step();assert(dem==0);''',
10: '''step();press(2);assert(dem==9999);assert(shown()==9999);
unsigned long before=elapsed;repeat(20);assert(dem==9999 && elapsed==before+400);
release();press(1);assert(dem==0);assert(last_select_mask==0xF0);''',
11: '''step();assert(MCUCR==10 && GICR==192);ext_int1_isr();assert(so==9999);
step();assert(shown()==9999);ext_int0_isr();step();assert(so==0 && shown()==0);
for(int k=0;k<10001;k++)ext_int0_isr();assert(so==1);''',
12: '''step();assert(elapsed==1000);assert(trace_port[0]==0xAA && trace_port[1]==0x55);
ext_int0_isr();assert(nua_chuky==9);unsigned long before=elapsed;step();assert(elapsed-before==900);
for(int k=0;k<100;k++)ext_int0_isr();assert(nua_chuky==1);
for(int k=0;k<100;k++)ext_int1_isr();assert(nua_chuky==20);
assert(MCUCR==10 && GICR==192);''',
13: '''for(int v=0;v<1024;v++){ADCW=v;step();assert(shown()==(v*50UL+511)/1023);assert(display_dp==4);}
assert(ADMUX==0 && ADCSRA==134);''',
14: '''for(int v=0;v<1024;v++){ADCW=v;step();assert(shown()==(v*500UL+511)/1023);assert(display_dp==2);}
assert(ADMUX==0 && ADCSRA==134);''',
15: '''ADCW=512;step();assert(so_le==2 && shown()==250 && display_dp==2);
press(1);assert(so_le==1 && shown()==25 && display_dp==4);
repeat(20);assert(so_le==1);release();press(1);assert(so_le==2 && shown()==250);
ADCW=1023;step();assert(shown()==500);''',
16: '''ADCW=0;step();assert(shown()==0);ADCW=51;step();assert(shown()==25);
ADCW=205;step();assert(shown()==100);assert(display_dp==0);
for(int v=0;v<1024;v++){ADCW=v;step();assert(shown()==(v*500UL+511)/1023);}''',
23: '''ADCW=1023;step();assert(kenh==0 && PORTD==1 && ADMUX==0 && shown()==5000 && display_dp==1);
for(int k=1;k<=16;k++){PINC=0xDF;step();step();assert(kenh==k%8);assert(ADMUX==k%8);assert(PORTD==(1<<(k%8)));repeat(3);assert(kenh==k%8);PINC=255;step();step();}
assert((PORTC&0x20)==0x20);''',
24: '''step();assert(dem==1234 && chay==0 && MCUCR==10);press(1);assert(chay==1);
repeat(49);assert(dem==1235);release();press(2);assert(chay==0);repeat(60);assert(dem==1235);
ext_int0_isr();assert(buoc_t==11);ext_int1_isr();assert(buoc_t==10);
for(int k=0;k<200;k++)ext_int1_isr();assert(buoc_t==2);
for(int k=0;k<200;k++)ext_int0_isr();assert(buoc_t==100);''',
25: '''step();assert(dem==1234 && MCUCR==15);press(1);repeat(49);assert(dem==1233);
release();press(1);assert(chay==0);repeat(60);assert(dem==1233);
ext_int0_isr();assert(buoc_t==11);ext_int1_isr();assert(buoc_t==10);
chay=1;dem=0;dem_ms=980;step();assert(dem==9999);''',
26: '''step();assert(dem==1234 && MCUCR==3 && GICR==64);ext_int0_isr();repeat(50);assert(dem==1235);
ext_int0_isr();repeat(100);assert(dem==1235 && dem_ms==0);
for(int k=0;k<30;k++){release();press(1);}assert(buoc_t==20);
for(int k=0;k<30;k++){release();press(2);}assert(buoc_t==2);
release();ext_int0_isr();repeat(10);assert(dem==1236);''',
27: '''step();assert(dem==1234);press(1);repeat(49);assert(dem==1235);
repeat(50);assert(dem==1236);release();press(2);repeat(100);assert(dem==1236);
chay=1;dem=9999;dem_ms=980;PIND=255;step();assert(dem==0);''',
28: '''step();press(1);repeat(49);assert(dem==1235 && chay==1);
repeat(50);assert(dem==1236 && chay==1);release();press(1);repeat(100);assert(dem==1236 && chay==0);''',
29: '''step();assert(dem==1234);PIND=254;repeat(29);assert(dem==1234);step();assert(dem==1235);
repeat(30);assert(dem==1236);PIND=255;repeat(100);assert(dem==1236 && dem_ms==0);
PIND=254;dem=9999;repeat(30);assert(dem==0);''',
30: '''repeat(50);assert(dem==1235);press(1);assert(buoc_t==11);
repeat(10);assert(buoc_t==11);release();press(2);assert(buoc_t==10);
dem=9999;dem_ms=980;step();assert(dem==0);
for(int k=0;k<110;k++){release();press(1);}assert(buoc_t==100);
for(int k=0;k<110;k++){release();press(2);}assert(buoc_t==2);''',
31: '''for(int mask=0;mask<1024;mask++){PIND=(unsigned char)~mask;PINA=(unsigned char)~(mask>>8);step();
int high=-1;for(int k=0;k<10;k++)if(mask&(1<<k))high=k;
assert(PORTC==(high<0?255:digits[high]));}'''
}

REGS = 'PORTA PORTB PORTC PORTD DDRA DDRB DDRC DDRD PINA PINB PINC PIND MCUCSR MCUCR GIFR GICR ADCSRA ADMUX'.split()
BITS = dict(JTD=7, ISC01=1, ISC00=0, ISC11=3, ISC10=2, INTF0=6, INTF1=7, INT0=6, INT1=7, ADEN=7, ADSC=6, ADPS2=2, ADPS1=1)

def portable(text):
    text = re.sub(r'#include <(?:mega16|delay)\.h>', '', text)
    text = re.sub(r'#asm\([^\n]*\)', '', text)
    text = re.sub(r'interrupt \[EXT_INT[01]\]', '', text)
    return text

def check_call(args):
    result = subprocess.run(args, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr

with tempfile.TemporaryDirectory(prefix='proteus_checks_') as temp:
    temp = Path(temp)
    for number, path in sorted(FILES.items()):
        code = path.read_text(encoding='utf-8')
        assert code.count('{') == code.count('}'), path.name
        globals_text = code.split('// Declare your global variables here\n', 1)[1].split('void main(void)', 1)[0]
        body = code.split('while (1)\n{\n', 1)[1].rsplit('\n}\n}', 1)[0]
        definitions = '\n'.join(f'#define {name} {value}' for name, value in BITS.items())
        registers = '\n'.join(f'unsigned char {name} = {255 if name.startswith("PIN") or name=="PORTC" else 0};' for name in REGS)
        shift = 4 if number in (9, 10) else 0
        support = f'''#include <assert.h>
#include <stdio.h>
{definitions}
{registers}
unsigned int ADCW;
unsigned long elapsed;
unsigned char digits[10]={{0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90}};
unsigned char trace_port[4096];unsigned int trace_ms[4096];int trace_count;
int display_digits[4], display_dp, last_select_mask;
void delay_ms(unsigned int ms){{
elapsed+=ms;
if(trace_count<4096){{trace_port[trace_count]=PORTC;trace_ms[trace_count++]=ms;}}
if(ms==5)for(int k=0;k<4;k++)if(PORTC&(1<<(k+{shift}))){{
last_select_mask|=1<<(k+{shift});
display_digits[k]=-1;
for(int d=0;d<10;d++)if((PORTB|0x80)==digits[d])display_digits[k]=d;
if((PORTB&0x80)==0)display_dp|=1<<k;else display_dp&=~(1<<k);
}}
}}
void delay_us(unsigned int us){{(void)us;}}
int shown(void){{int n=0;for(int k=0;k<4;k++){{assert(display_digits[k]>=0);n=n*10+display_digits[k];}}return n;}}
'''
        tokens = set(re.findall(r'\b[A-Z][A-Z0-9_]*\b', re.sub(r'/\*.*?\*/|//[^\n]*', '', portable(code), flags=re.S)))
        extra = '\n'.join(f'unsigned int {name};' for name in sorted(tokens-set(REGS)-set(BITS)-{'ADCW'}))
        syntax_file = temp / f'syntax_{number}.c'
        syntax_file.write_text(support + '\n' + extra + '\n' + portable(code).replace('void main(void)', 'void firmware(void)'), encoding='utf-8')
        check_call([GCC, '-std=c99', '-fsyntax-only', str(syntax_file)])
        body = portable(body)
        globals_text = portable(globals_text).replace('while (ADCSRA & (1 << ADSC));', 'ADCSRA &= ~(1 << ADSC);')
        harness = support + '\n' + globals_text + '''
void step(void){
static unsigned char maden[10]={0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90};
static char i=1;
''' + body + '''
}
void repeat(int n){while(n--)step();}
void press(unsigned char mask){PIND=(unsigned char)~mask;step();step();}
void release(void){PIND=255;step();step();}
int main(void){
''' + TESTS[number] + '\nputs("PASS");return 0;}\n'
        c_path = temp / f'test_{number}.c'
        exe_path = temp / f'test_{number}.exe'
        c_path.write_text(harness, encoding='utf-8')
        check_call([GCC, '-std=c99', '-O0', str(c_path), '-o', str(exe_path)])
        check_call([str(exe_path)])
        print(f'PASS bai_{number:02d}: C syntax adaptation + behavior assertions')
print('PASS 25/25. Hardware registers, ADC-ready, interrupts and delays are emulated; this is not a CodeVisionAVR build or Proteus simulation.')
