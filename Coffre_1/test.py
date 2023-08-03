from machine import UART, Pin
import time

uart = UART(1, baudrate=115200, tx=17, rx=16)

for i in range(10):
    uart.write("hello")
    time.sleep(0.1)
    print(uart.readline())
    time.sleep(0.1)
