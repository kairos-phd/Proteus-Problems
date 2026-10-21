/****
 * DC2DT29 - De 43, Cau 1. Kind: toggle8
 * ATmega16, 8 MHz, CodeVisionAVR. Compile ONLY this file in its project.
 * Source wording: ../problems.json, set 43, q1.
 * Common-anode segments active LOW; digit enables active HIGH.
 * See ../README.md for pin assignments, defaults, JTAG fuse and test limits.
 * Unspecified choices are documented in README.md; original wording is retained.
 ****/
#include <mega16.h>
#include <delay.h>

#define BUTTON_COUNT 8
#define REPEAT_MS 0
#define REPEAT_MASK 255U
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
    return (unsigned char)~PINA;
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
    value ^= keys;
}

void advance_time(unsigned int milliseconds)
{
    (void)milliseconds;
}

void render_display(void)
{
    PORTD = (unsigned char)~value;
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
    render_display();
    SREG = saved_sreg;
}

void initialize(void)
{
    unsigned char i;
    #asm("cli")
    DDRA = 0x00; PORTA = 0xFF;
    DDRB = 0x00; PORTB = 0xFF;
    DDRC = 0x00; PORTC = 0xFF;
    DDRD = 0xFF; PORTD = 0xFF;
    value = 0; period_ms = 1000; elapsed_ms = 0; running = 0;
    stable_keys = 0; display_dp = 0; scan_index = 0;
    channel = 0; precision = 0; temperature_mode = 0;
    for (i = 0; i < 10; ++i)
    {
        button_state[i] = 0; button_filter[i] = 0; button_age[i] = 0;
    }
    TCCR0 = 0; TCCR2 = 0; TIMSK = 0;
    MCUCR = 0x00; GICR = 0x00; GIFR = 0x00;
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
