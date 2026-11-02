from machine import I2C, Pin
from math import sqrt
import utime
from imu import MPU6050

# Sensor on I2C bus 1: SDA = GPIO6 (D4), SCL = GPIO7 (D5)
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
mpu = MPU6050(i2c)

# RGB LED on D0, D1, D2 (same pins as in the course code)
red = Pin(26, Pin.OUT)
green = Pin(27, Pin.OUT)
blue = Pin(28, Pin.OUT)

# Colors from calm to wild, each as (red, green, blue)
colors = [
    (0, 0, 1),   # calm = blue
    (0, 1, 0),   # medium = green
    (1, 0, 0),   # wild = red
]

# Upper limit of the smoothed restlessness value
# Use the same number as in your min(smoothed, ...) from step 3
MAX_VALUE = 0.7


def read_accelerometer():
    accel = mpu.accel
    return accel.x, accel.y, accel.z


def main():
    smoothed = 0
    while True:
        ax, ay, az = read_accelerometer()

        # total strength of the acceleration (about 1 g when still)
        magnitude = sqrt(ax ** 2 + ay ** 2 + az ** 2)

        # distance from the resting value
        restlessness = abs(magnitude - 1.055)

        # smoothing and upper limit
        smoothed = 0.9 * smoothed + 0.1 * restlessness
        limited = min(smoothed, MAX_VALUE)

        # 0 = calm ... 1 = maximum, then pick a color
        level = limited / MAX_VALUE
        index = min(int(level * len(colors)), len(colors) - 1)

        red.value(colors[index][0])
        green.value(colors[index][1])
        blue.value(colors[index][2])

        print(limited)
        utime.sleep(0.1)


if __name__ == "__main__":
    main()