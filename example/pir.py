from machine import Pin
from utime import sleep_ms

pir = Pin(20, Pin.IN)

while(True):
    print(pir.value())
    sleep_ms(100)
