from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

max_count = 500

@asm_pio(sideset_init=PIO.OUT_LOW)
def pwm_prog():
    pull(noblock) .side(0)
    mov(x, osr) 
    mov(y, isr) 
    label("pwmloop")
    jmp(x_not_y, "skip")
    nop()         .side(1)
    label("skip")
    jmp(y_dec, "pwmloop")
    

pwm_sm = StateMachine(0, pwm_prog, freq=10000000, sideset_base=Pin(25))

pwm_sm.put(max_count)
pwm_sm.exec("pull()")
pwm_sm.exec("mov(isr, osr)")
pwm_sm.active(1)

while True:
    for i in range(500):
        pwm_sm.put(i)
        sleep(0.001)