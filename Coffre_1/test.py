from machine import UART
import time

uart = UART(0, baudrate=115200, tx=17, rx=16)

for i in range(10):
    uart.write("hello")
    time.sleep(0.1)
    print(uart.read(16))
    time.sleep(0.1)
