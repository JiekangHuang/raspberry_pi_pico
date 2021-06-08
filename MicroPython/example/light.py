from machine import ADC
from utime import sleep_ms

adc = ADC(26)

while(True):
    print(adc.read_u16())
    sleep_ms(100)
