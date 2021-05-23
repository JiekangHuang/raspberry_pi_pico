from machine import Pin, ADC, PWM
from utime import sleep_ms

adc = ADC(26)

pwm = PWM(Pin(20))
pwm.freq(1000)

while(True):
    pwm.duty_u16(adc.read_u16())
    sleep_ms(100)
