from machine import Pin

while True:
    pir = Pin(20, Pin.IN)
    print(pir.value())