from machine import Pin
from utime import sleep_ms

red = Pin(16, Pin.OUT)
yellow = Pin(18, Pin.OUT)
green = Pin(20, Pin.OUT)

while(True):
    red.on()
    sleep_ms(5000)
    red.off()
    yellow.on()
    sleep_ms(1000)
    yellow.off()
    green.on()
    sleep_ms(5000)
    green.off()