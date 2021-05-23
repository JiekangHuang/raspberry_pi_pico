from machine import Pin

led = Pin(18, Pin.OUT)
btn = Pin(20, Pin.IN)

while(True):
    if(btn.value() == False):
        led.on()
    else:
        led.off()
