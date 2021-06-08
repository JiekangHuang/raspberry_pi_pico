from machine import Pin,PWM
import time

def alarmBeep(pwm):
   pwm.freq(1000)     #設定頻率為 1KHz    
   pwm.duty_u16(512)      #設定工作週期為 50%
   time.sleep(1)        
   pwm.deinit()          
   time.sleep(2)         

pwm=PWM(Pin(20))

while True:
   alarmBeep(pwm)