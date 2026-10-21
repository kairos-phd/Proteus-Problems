/****
 * DC2DT29 - De 03, Cau 2. Kind: timer_start
 * ATmega16, 8 MHz, CodeVisionAVR. Compile ONLY this file in its project.
 * Source wording: ../problems.json, set 3, q2.
 * Common-anode segments active LOW; digit enables active HIGH.
 * See ../README.md for pin assignments, defaults, JTAG fuse and test limits.
 * Unspecified choices are documented in README.md; original wording is retained.
 ****/
#include <mega16.h>
#include <delay.h>

#define BUTTON_COUNT 3
#define REPEAT_MS 0
#define REPEAT_MASK 3U
#define DIGIT_COUNT 4
unsigned char segments[10] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90};
volatile unsigned int value = 1111;
volatile unsigned int period_ms = 500, elapsed_ms;
volatile unsigned char running = 0;
unsigned char display_digits[4], display_dp, scan_index;
volatile unsigned char channel;
unsigned char precision, temperature_mode;

unsigned int raw_buttons(void)
{
    return (unsigned char)~PINB & 7U;
}

/* Active-low buttons: 20 consecutive 1 ms samples; independent debounce.
   A held key repeats only when REPEAT_MS is nonzero. */
unsigned char button_state[10], button_filter[10];
unsigned int button_age[10];
unsigned int stable_keys;
unsigned int sample_buttons(void)
{
#if BUTTON_COUNT > 0
    unsigned char i;
    unsigned int raw, bit, events;
    raw = raw_buttons();
    events = 0;
    for (i = 0; i < BUTTON_COUNT; ++i)
    {
        bit = 1U << i;
        if (((raw & bit) != 0) != button_state[i])
        {
            if (++button_filter[i] >= 20)
            {
                button_filter[i] = 0;
                button_state[i] = (raw & bit) != 0;
                button_age[i] = 0;
                if (button_state[i]) events |= bit;
            }
        }
        else
        {
            button_filter[i] = 0;
#if REPEAT_MS > 0
            if (button_state[i] && (REPEAT_MASK & bit))
            {
                if (++button_age[i] >= REPEAT_MS)
                {
                    button_age[i] = 0;
                    events |= bit;
                }
            }
#endif
        }
    }
    stable_keys = 0;
    for (i = 0; i < BUTTON_COUNT; ++i)
        if (button_state[i]) stable_keys |= 1U << i;
    return events;
#else
    return 0;
#endif
}

void change_period(signed char direction)
{
    if (direction > 0)
    {
        if (period_ms <= 1900) period_ms += 100;
        else period_ms = 2000;
    }
    else
    {
        if (period_ms >= 200) period_ms -= 100;
        else period_ms = 100;
    }
    /* Preserve phase: repeated speed changes must not starve movement. */
}

void handle_buttons(unsigned int keys)
{
    if (keys == 1 && value < 9000) ++value;
    if (keys == 2 && value > 1000) --value;
    if (keys & 4) { running = 1; elapsed_ms = 0; }
}

void advance_time(unsigned int milliseconds)
{
    if (!running) { elapsed_ms = 0; return; }
    elapsed_ms += milliseconds;
    while (running && elapsed_ms >= period_ms)
    {
        elapsed_ms -= period_ms;
        value = value >= 9000 ? 1000 : value + 1;
    }
}

void render_number(void)
{
    unsigned char i;
    unsigned int number;
    number = value;
    for (i = DIGIT_COUNT; i > 0; --i)
    {
        display_digits[i-1] = number % 10;
        number /= 10;
    }
}
void scan_display(void)
{
    unsigned char pattern;
    /* Blank every digit before changing segments to prevent ghosting. */
    PORTA &= 0x0F;
    pattern = segments[display_digits[scan_index]];
    if (display_dp & (1U << scan_index)) pattern &= 0x7F;
    PORTC = pattern;
    PORTA |= 1U << (scan_index + 4);
    if (++scan_index >= DIGIT_COUNT) scan_index = 0;
}

void render_display(void)
{
    render_number();
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
    advance_time(4);
}

interrupt [EXT_INT0] void ext_int0_isr(void)
{
    running = 0; elapsed_ms = 0;
}

void tick_1ms(void)
{
    unsigned char saved_sreg;
    unsigned int events;
    /* Atomic access to shared 16-bit counters and the scan buffer on an 8-bit MCU. */
    saved_sreg = SREG;
    #asm("cli")
    events = sample_buttons();
    handle_buttons(events);
    render_display();
    scan_display();
    SREG = saved_sreg;
}

void initialize(void)
{
    unsigned char i;
    #asm("cli")
    DDRA = 0xF0; PORTA = 0x0F;
    DDRB = 0x00; PORTB = 0xFF;
    DDRC = 0xFF; PORTC = 0xFF;
    DDRD = 0x00; PORTD = 0xFF;
    value = 1111; period_ms = 500; elapsed_ms = 0; running = 0;
    stable_keys = 0; display_dp = 0; scan_index = 0;
    channel = 0; precision = 0; temperature_mode = 0;
    for (i = 0; i < 10; ++i)
    {
        button_state[i] = 0; button_filter[i] = 0; button_age[i] = 0;
    }
    TCCR0 = 0; TCCR2 = 0; TIMSK = 0;
    MCUCR = 0x02; GICR = 0x40; GIFR = 0x40;
    TCNT0 = 131; TCCR0 = 4; TIMSK |= 0x01;
    render_display();
    #asm("sei")
}

void main(void)
{
    initialize();
    while (1)
    {
        delay_ms(1);
        tick_1ms();
    }
}
