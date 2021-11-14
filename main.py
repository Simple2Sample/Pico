from machine import Pin
import time
led = Pin(28,Pin.OUT)

print("Hello World")
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
