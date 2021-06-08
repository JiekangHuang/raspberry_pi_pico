from machine import Pin, I2C
from sht31 import SHT31
from ssd1306 import SSD1306_I2C

WIDTH = 128    # oled 顯示寬度
HEIGHT = 32     # oled 顯示高度

oled_i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled = SSD1306_I2C(WIDTH, HEIGHT, oled_i2c)

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
sensor = SHT31(i2c, addr=0x44)

while(True):
    oled.fill(0)  # 清除畫面
    t = round(sensor.get_temp_humi()[0], 2)
    h = round(sensor.get_temp_humi()[1], 2)

    oled.text("Temp: ", 0, 10)
    oled.text(str(t), 50, 10)
    oled.text("*C", 90, 10)

    oled.text("Humi: ", 0, 20)
    oled.text(str(h), 50, 20)
    oled.text("%", 90, 20)
    oled.show()
