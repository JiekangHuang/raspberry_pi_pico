from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

pwm = PWM(Pin(20))
pwm.freq(50)

while(True):
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)