from machine import Pin, ADC, PWM

adc = ADC(26)

pwm = PWM(Pin(20))
pwm.freq(50)

def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

while(True):
    servo_duty = convert(adc.read_u16(), 0, 65535, 1638, 8191)
    pwm.duty_u16(servo_duty)