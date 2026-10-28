
from machine import Pin
import time

# LEDs
red = Pin(26, Pin.OUT)
yellow = Pin(27, Pin.OUT)
green = Pin(28, Pin.OUT)

# Button on D3, connected to GND
button = Pin(29, Pin.IN, Pin.PULL_UP)

# Time each light stays on (milliseconds)
INTERVAL = 1000

# Traffic light sequence
sequence = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Yellow
    (0, 0, 1),  # Green
]

# Start with all lights off
red.value(0)
yellow.value(0)
green.value(0)

step = 0
last_change = time.ticks_ms()

while True:
    if button.value() == 0:  # Button is pressed
        now = time.ticks_ms()

        if time.ticks_diff(now, last_change) >= INTERVAL:
            step = (step + 1) % len(sequence)

            red.value(sequence[step][0])
            yellow.value(sequence[step][1])
            green.value(sequence[step][2])

            last_change = now

    else:  # Button released
        red.value(0)
        yellow.value(0)
        green.value(0)

        step = 0
        last_change = time.ticks_ms()

    time.sleep_ms(10)