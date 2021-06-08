import time

import board
import analogio
import pwmio

pwm = pwmio.PWMOut(board.GP20, frequency=1000)

while True:
    pwm.duty_cycle = 32512
    time.sleep(1)
    pwm.duty_cycle = 0
    time.sleep(1)