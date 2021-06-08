from machine import Pin, I2C
import sht31
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq =400000)
sensor = sht31.SHT31(i2c, addr=0x44)
while(True):
    value = sensor.get_temp_humi()
    print(value)