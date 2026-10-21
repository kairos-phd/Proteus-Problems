/****
 * DC2DT29 - De 39, Cau 2. Kind: adc_channel_button
 * ATmega16, 8 MHz, CodeVisionAVR. Compile ONLY this file in its project.
 * Source wording: ../problems.json, set 39, q2.
 * Common-anode segments active LOW; digit enables active HIGH.
 * See ../README.md for pin assignments, defaults, JTAG fuse and test limits.
 * Unspecified choices are documented in README.md; original wording is retained.
 ****/
#include <mega16.h>
#include <delay.h>

#define BUTTON_COUNT 1
#define REPEAT_MS 0
#define REPEAT_MASK 1U
#define DIGIT_COUNT 4
unsigned char segments[10] = {0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xF8,0x80,0x90};
volatile unsigned int value = 0;
volatile unsigned int period_ms = 1000, elapsed_ms;
volatile unsigned char running = 0;
unsigned char display_digits[4], display_dp, scan_index;
volatile unsigned char channel;
unsigned char precision, temperature_mode;

unsigned int raw_buttons(void)
{
    return (unsigned char)~PIND & 1U;
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
    if (keys & 1) channel = (channel + 1) % 3;
}

void advance_time(unsigned int milliseconds)
{
    (void)milliseconds;
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

unsigned int read_adc(unsigned char input)
{
    /* AVCC = 5 V reference, F_ADC = 8 MHz / 64 = 125 kHz. */
    ADMUX = 0x40 | input;
    delay_us(10);
    ADCSRA |= 0x40;
    while (ADCSRA & 0x40);
    return ADCW;
}
void update_measurement(void)
{
    unsigned int raw;
    raw = read_adc(channel);
    value = (raw * (precision ? 500UL : 50UL) + 511) / 1023;
    display_dp = precision ? 2 : 4;
    PORTB = segments[channel];
}

void render_display(void)
{
    render_number();
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
    advance_time(1);
    update_measurement();
    render_display();
    scan_display();
    SREG = saved_sreg;
}

void initialize(void)
{
    unsigned char i;
    #asm("cli")
    DDRA = 0xF0; PORTA = 0x00;
    DDRB = 0xFF; PORTB = 0xFF;
    DDRC = 0xFF; PORTC = 0xFF;
    DDRD = 0x00; PORTD = 0xFF;
    value = 0; period_ms = 1000; elapsed_ms = 0; running = 0;
    stable_keys = 0; display_dp = 0; scan_index = 0;
    channel = 0; precision = 0; temperature_mode = 0;
    for (i = 0; i < 10; ++i)
    {
        button_state[i] = 0; button_filter[i] = 0; button_age[i] = 0;
    }
    TCCR0 = 0; TCCR2 = 0; TIMSK = 0;
    MCUCR = 0x00; GICR = 0x00; GIFR = 0x00;
    ADMUX = 0x40;
    ADCSRA = 0x86;
    update_measurement();
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
