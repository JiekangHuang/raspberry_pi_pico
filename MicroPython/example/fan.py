from machine import Pin, ADC, PWM

adc = ADC(26)

btn = Pin(18, Pin.IN)

pwm_a = PWM(Pin(20))
pwm_b = PWM(Pin(21))
pwm_a.freq(1000)
pwm_b.freq(1000)

state = False
while(True):
    if(btn.value() == False):
        while(btn.value() == False):
            pass
        state = not state
    if(state):
        pwm_a.duty_u16(adc.read_u16())
        pwm_b.duty_u16(0)
    else:
        pwm_b.duty_u16(adc.read_u16())
        pwm_a.duty_u16(0)

