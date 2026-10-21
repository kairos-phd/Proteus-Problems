/*******************************************************
This program was created by the
CodeWizardAVR V3.12 Advanced
Automatic Program Generator
© Copyright 1998-2014 Pavel Haiduc, HP InfoTech s.r.l.
http://www.hpinfotech.com

Project :
Version :
Date    : 8/24/2026
Author  :
Company :
Comments:

Chip type               : ATmega16
Program type            : Application
AVR Core Clock frequency: 8.000000 MHz
Memory model            : Small
External RAM size       : 0
Data Stack size         : 256
*******************************************************/

#include <mega16.h>
#include <delay.h>

// Declare your global variables here
// DC2DT29 - De 33, Cau 2. Kind: timer_auto_dec
// Mot file cau_1.c hoac cau_2.c cho moi project. Xem ../README.md.
unsigned char trangthai_ngat;
unsigned int nhan;
#define SO_NUT 3
#define LAP_NUT_MS 0
#define MAT_NA_LAP 7U
#define SO_LED 4
unsigned char ma7doan[10] =
{
    0xC0, 0xF9, 0xA4, 0xB0, 0x99,
    0x92, 0x82, 0xF8, 0x80, 0x90
};
volatile unsigned int dem = 1234;
volatile unsigned int thoigian = 500, dem_ms;
volatile unsigned char chay = 0;
unsigned char sohienthi[4], daucham, vitriquet;
volatile unsigned char kenh;
unsigned char dophangiai, donhietdo;

unsigned int docchan(void)
{
    return (unsigned char)~PINB & 7U;
}

/* Active-low buttons: 20 consecutive 1 ms samples; independent debounce.
   A held key repeats only when LAP_NUT_MS is nonzero. */
unsigned char nut_on[10], locnut[10];
unsigned int giu_ms[10];
unsigned int nut_giu;
unsigned int docnut(void)
{
#if SO_NUT > 0
    unsigned char i;
    unsigned int raw, bit, events;
    raw = docchan();
    events = 0;
    for (i = 0; i < SO_NUT; ++i)
    {
        bit = 1U << i;
        if (((raw & bit) != 0) != nut_on[i])
        {
            if (++locnut[i] >= 20)
            {
                locnut[i] = 0;
                nut_on[i] = (raw & bit) != 0;
                giu_ms[i] = 0;
                if (nut_on[i]) events |= bit;
            }
        }
        else
        {
            locnut[i] = 0;
#if LAP_NUT_MS > 0
            if (nut_on[i] && (MAT_NA_LAP & bit))
            {
                if (++giu_ms[i] >= LAP_NUT_MS)
                {
                    giu_ms[i] = 0;
                    events |= bit;
                }
            }
#endif
        }
    }
    nut_giu = 0;
    for (i = 0; i < SO_NUT; ++i)
        if (nut_on[i]) nut_giu |= 1U << i;
    return events;
#else
    return 0;
#endif
}

void doithoigian(signed char direction)
{
    if (direction > 0)
    {
        if (thoigian <= 1900) thoigian += 100;
        else thoigian = 2000;
    }
    else
    {
        if (thoigian >= 200) thoigian -= 100;
        else thoigian = 100;
    }
    /* Preserve phase: repeated speed changes must not starve movement. */
}

void xulynut(unsigned int keys)
{
    if (keys == 1 && dem < 9999) ++dem;
    if (keys == 2 && dem > 0) --dem;
    if (keys & 4) { chay = 1; dem_ms = 0; }
}

void demthoigian(unsigned int milliseconds)
{
    if (!chay) { dem_ms = 0; return; }
    dem_ms += milliseconds;
    while (chay && dem_ms >= thoigian)
    {
        dem_ms -= thoigian;
        if (dem > 0) --dem;
        if (dem == 0) chay = 0;
    }
}

void capnhatled(void)
{
    unsigned char i;
    unsigned int number;
    number = dem;
    for (i = SO_LED; i > 0; --i)
    {
        sohienthi[i-1] = number % 10;
        number /= 10;
    }
}
void quetled(void)
{
    unsigned char pattern;
    /* Blank every digit before changing ma7doan to prevent ghosting. */
    PORTA &= 0x0F;
    pattern = ma7doan[sohienthi[vitriquet]];
    if (daucham & (1U << vitriquet)) pattern &= 0x7F;
    PORTC = pattern;
    PORTA |= 1U << (vitriquet + 4);
    if (++vitriquet >= SO_LED) vitriquet = 0;
}

void hienthi(void)
{
    capnhatled();
}

/* Timer 0 NORMAL mode. F_CPU=8 MHz, prescaler=256.
   F_timer=31250 Hz, 125 counts/overflow with preload 131.
   One interrupt is 4 ms; 125 interrupts = 500 ms exactly in timer counts.
   Add the preload to TCNT0 to compensate ISR entry latency in timer ticks.
   No delay, ADC, or display multiplexing occurs in this ISR.
   Timing is nominal: clock accuracy and interrupt latency require Proteus/hardware measurement. */
interrupt [TIM0_OVF] void timer0_overflow(void)
{
    TCNT0 += 131;
    demthoigian(4);
}

/* Timer 2 NORMAL: 8 MHz / 64 = 125 kHz; 250 counts = 2 ms/digit.
   Four digits form an 8 ms frame (125 Hz). */
interrupt [TIM2_OVF] void timer2_overflow(void)
{
    TCNT2 += 6;
    quetled();
}

void main(void)
{
    unsigned char i;

    #asm("cli")

    // Input/Output Ports initialization
    // Port A initialization
    // Function: Bit7=Out Bit6=Out Bit5=Out Bit4=Out Bit3=In Bit2=In Bit1=In Bit0=In
    DDRA=(1<<DDA7) | (1<<DDA6) | (1<<DDA5) | (1<<DDA4) | (0<<DDA3) | (0<<DDA2) | (0<<DDA1) | (0<<DDA0);
    // State: Bit7=0 Bit6=0 Bit5=0 Bit4=0 Bit3=P Bit2=P Bit1=P Bit0=P
    PORTA=(0<<PORTA7) | (0<<PORTA6) | (0<<PORTA5) | (0<<PORTA4) | (1<<PORTA3) | (1<<PORTA2) | (1<<PORTA1) | (1<<PORTA0);

    // Port B initialization
    // Function: Bit7=In Bit6=In Bit5=In Bit4=In Bit3=In Bit2=In Bit1=In Bit0=In
    DDRB=(0<<DDB7) | (0<<DDB6) | (0<<DDB5) | (0<<DDB4) | (0<<DDB3) | (0<<DDB2) | (0<<DDB1) | (0<<DDB0);
    // State: Bit7=P Bit6=P Bit5=P Bit4=P Bit3=P Bit2=P Bit1=P Bit0=P
    PORTB=(1<<PORTB7) | (1<<PORTB6) | (1<<PORTB5) | (1<<PORTB4) | (1<<PORTB3) | (1<<PORTB2) | (1<<PORTB1) | (1<<PORTB0);

    // Port C initialization
    // Function: Bit7=Out Bit6=Out Bit5=Out Bit4=Out Bit3=Out Bit2=Out Bit1=Out Bit0=Out
    DDRC=(1<<DDC7) | (1<<DDC6) | (1<<DDC5) | (1<<DDC4) | (1<<DDC3) | (1<<DDC2) | (1<<DDC1) | (1<<DDC0);
    // State: Bit7=1 Bit6=1 Bit5=1 Bit4=1 Bit3=1 Bit2=1 Bit1=1 Bit0=1
    PORTC=(1<<PORTC7) | (1<<PORTC6) | (1<<PORTC5) | (1<<PORTC4) | (1<<PORTC3) | (1<<PORTC2) | (1<<PORTC1) | (1<<PORTC0);

    // Port D initialization
    // Function: Bit7=In Bit6=In Bit5=In Bit4=In Bit3=In Bit2=In Bit1=In Bit0=In
    DDRD=(0<<DDD7) | (0<<DDD6) | (0<<DDD5) | (0<<DDD4) | (0<<DDD3) | (0<<DDD2) | (0<<DDD1) | (0<<DDD0);
    // State: Bit7=P Bit6=P Bit5=P Bit4=P Bit3=P Bit2=P Bit1=P Bit0=P
    PORTD=(1<<PORTD7) | (1<<PORTD6) | (1<<PORTD5) | (1<<PORTD4) | (1<<PORTD3) | (1<<PORTD2) | (1<<PORTD1) | (1<<PORTD0);

    // Timer/Counter 0 initialization
    // Clock source: System Clock
    // Clock value: 31.250 kHz
    // Mode: Normal top=0xFF
    // OC0 output: Disconnected
    TCCR0=(0<<WGM00) | (0<<COM01) | (0<<COM00) | (0<<WGM01) | (1<<CS02) | (0<<CS01) | (0<<CS00);
    TCNT0=0x83;
    OCR0=0x00;

    // Timer/Counter 1 initialization
    // Clock source: System Clock
    // Clock value: Timer1 Stopped
    // Mode: Normal top=0xFFFF
    // OC1A output: Disconnected
    // OC1B output: Disconnected
    // Noise Canceler: Off
    // Input Capture on Falling Edge
    // Timer1 Overflow Interrupt: Off
    // Input Capture Interrupt: Off
    // Compare A Match Interrupt: Off
    // Compare B Match Interrupt: Off
    TCCR1A=(0<<COM1A1) | (0<<COM1A0) | (0<<COM1B1) | (0<<COM1B0) | (0<<WGM11) | (0<<WGM10);
    TCCR1B=(0<<ICNC1) | (0<<ICES1) | (0<<WGM13) | (0<<WGM12) | (0<<CS12) | (0<<CS11) | (0<<CS10);
    TCNT1H=0x00;
    TCNT1L=0x00;
    ICR1H=0x00;
    ICR1L=0x00;
    OCR1AH=0x00;
    OCR1AL=0x00;
    OCR1BH=0x00;
    OCR1BL=0x00;

    // Timer/Counter 2 initialization
    // Clock source: System Clock
    // Clock value: 125.000 kHz
    // Mode: Normal top=0xFF
    // OC2 output: Disconnected
    ASSR=0<<AS2;
    TCCR2=(0<<PWM2) | (0<<COM21) | (0<<COM20) | (0<<CTC2) | (1<<CS22) | (0<<CS21) | (0<<CS20);
    TCNT2=0x06;
    OCR2=0x00;

    // Timer(s)/Counter(s) Interrupt(s) initialization
    TIMSK=(0<<OCIE2) | (1<<TOIE2) | (0<<TICIE1) | (0<<OCIE1A) | (0<<OCIE1B) | (0<<TOIE1) | (0<<OCIE0) | (1<<TOIE0);

    // External Interrupt(s) initialization
    // INT0: Off
    // INT1: Off
    // INT2: Off
    MCUCR=(0<<ISC11) | (0<<ISC10) | (0<<ISC01) | (0<<ISC00);
    GIFR=(0<<INTF1) | (0<<INTF0) | (0<<INTF2);
    GICR=(0<<INT1) | (0<<INT0) | (0<<INT2);

    // USART initialization
    // USART disabled
    UCSRB=(0<<RXCIE) | (0<<TXCIE) | (0<<UDRIE) | (0<<RXEN) | (0<<TXEN) | (0<<UCSZ2) | (0<<RXB8) | (0<<TXB8);

    // Analog Comparator initialization
    // Analog Comparator: Off
    // The Analog Comparator's positive input is
    // connected to the AIN0 pin
    // The Analog Comparator's negative input is
    // connected to the AIN1 pin
    ACSR=(1<<ACD) | (0<<ACBG) | (0<<ACO) | (0<<ACI) | (0<<ACIE) | (0<<ACIC) | (0<<ACIS1) | (0<<ACIS0);
    SFIOR=(0<<ACME);

    // ADC initialization
    // ADC disabled
    ADCSRA=(0<<ADEN) | (0<<ADSC) | (0<<ADATE) | (0<<ADIF) | (0<<ADIE) | (0<<ADPS2) | (0<<ADPS1) | (0<<ADPS0);

    // SPI initialization
    // SPI disabled
    SPCR=(0<<SPIE) | (0<<SPE) | (0<<DORD) | (0<<MSTR) | (0<<CPOL) | (0<<CPHA) | (0<<SPR1) | (0<<SPR0);

    // TWI initialization
    // TWI disabled
    TWCR=(0<<TWEA) | (0<<TWSTA) | (0<<TWSTO) | (0<<TWEN) | (0<<TWIE);

    // Program variables initialization
    dem = 1234; thoigian = 500; dem_ms = 0; chay = 0;
    nut_giu = 0; daucham = 0; vitriquet = 0;
    kenh = 0; dophangiai = 0; donhietdo = 0;
    for (i = 0; i < 10; ++i)
    {
        nut_on[i] = 0; locnut[i] = 0; giu_ms[i] = 0;
    }
    hienthi();

    // Global interrupt enable
    #asm("sei")

while (1)
{
    delay_ms(1);
    /* Atomic access to shared 16-bit counters and the scan buffer on an 8-bit MCU. */
    trangthai_ngat = SREG;
    #asm("cli")
    nhan = docnut();
    xulynut(nhan);
    hienthi();
    SREG = trangthai_ngat;
}
}
