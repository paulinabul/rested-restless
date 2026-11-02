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

# Sensitivity: the lower the numbers, the earlier the color changes
GREEN_AT = 0.08   # from this value on: green
RED_AT = 0.17      # from this value on: red

# Smoothing: 0.9 = very smooth and slow, 0.5 = fast and jumpy
SMOOTHING = 0.7


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

        # smoothing
        smoothed = SMOOTHING * smoothed + (1 - SMOOTHING) * restlessness

        # pick the color: blue = calm, green = medium, red = wild
        if smoothed >= RED_AT:
            color = (1, 0, 0)
        elif smoothed >= GREEN_AT:
            color = (0, 1, 0)
        else:
            color = (0, 0, 1)

        red.value(color[0])
        green.value(color[1])
        blue.value(color[2])

        print(smoothed)
        utime.sleep(0.05)


if __name__ == "__main__":
    main()