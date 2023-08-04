from machine import UART
import time

uart = UART(1, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)

for i in range(10):
    uart.write("hello")
    time.sleep(0.1)
    print(uart.readline())
    time.sleep(0.1)
