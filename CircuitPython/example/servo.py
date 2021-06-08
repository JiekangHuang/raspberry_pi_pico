import board
import analogio
import pwmio

potentiometer = analogio.AnalogIn(board.GP26)
pwm = pwmio.PWMOut(board.GP20, frequency=50)

def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

while True:
    servo_duty = convert(potentiometer.value, 0, 65535, 1638, 8191)
    pwm.duty_cycle = servo_duty