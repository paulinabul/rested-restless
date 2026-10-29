from machine import Pin
import time

red = Pin(26, Pin.OUT)
green = Pin(27, Pin.OUT)
blue = Pin(28, Pin.OUT)

# all off
red.value(0)
green.value(0)
blue.value(0)

# red for 2 seconds
red.value(1)
time.sleep(2)
red.value(0)

# blue for 2 seconds
blue.value(1)
time.sleep(2)
blue.value(0)

# green for 2 seconds
green.value(1)
time.sleep(2)
green.value(0)