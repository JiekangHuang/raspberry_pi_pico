from machine import Pin
from utime import sleep_ms

sw = Pin(20, Pin.IN)

while(True):
    print(sw.value())
    sleep_ms(100)
