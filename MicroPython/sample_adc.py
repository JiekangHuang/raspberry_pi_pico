import machine
import utime

analog_value = machine.ADC(26)

while True:
    reading = analog_value.read_u16()     
    print(reading)
    # utime.sleep(0.2)