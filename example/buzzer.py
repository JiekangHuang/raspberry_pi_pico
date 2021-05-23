from machine import Pin, PWM
from utime import sleep_ms

pwm = PWM(Pin(20))

pwm.freq(1000)

while True:
    pwm.duty_u16(32512)
    sleep_ms(1000)
    pwm.deinit()
    sleep_ms(2000)
