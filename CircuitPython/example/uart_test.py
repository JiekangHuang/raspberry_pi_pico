import busio
import board
import time

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate = 115200)

while(True):
    uart.write(b"AT\r\n")
    time.sleep(0.1)
    if(uart.in_waiting > 0):
        print(uart.readline())
