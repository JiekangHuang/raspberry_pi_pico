import time, _thread, machine

data = ""

def task(n, delay):
    led = machine.Pin(25, machine.Pin.OUT)
    for i in range(n):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
        data = i
    print('done')

_thread.start_new_thread(task, (10, 0.5))

for i in range(10):
    print(data)
    time.sleep(1.5)