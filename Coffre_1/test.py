from machine import UART
import time

uart = UART(2, baudrate=115200, tx=17, rx=16)
uart.write("hello")
for i in range(1000):
    print(uart.read(16))
    time.sleep(0.1)
