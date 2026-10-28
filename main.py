from machine import I2C, Pin
import utime
from imu import MPU6050
from math import sqrt

# Initialize I2C interface (I2C1) with SDA on GPIO6 (D4) and SCL on GPIO7 (D5)
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

# Initialize the MPU-6050 sensor
mpu = MPU6050(i2c)

def read_accelerometer():
   """Reads accelerometer data and returns it as a tuple (x, y, z)."""
   accel = mpu.accel
   return accel.x, accel.y, accel.z

def read_gyroscope():
   """Reads gyroscope data and returns it as a tuple (x, y, z)."""
   gyro = mpu.gyro
   return gyro.x, gyro.y, gyro.z

def main():
   """Main loop to read and print sensor data."""
   smoothed = 0
   while True:
      # Read accelerometer data
      ax, ay, az = read_accelerometer()
      magnitude = sqrt(ax ** 2 + ay ** 2 + az ** 2)
      restlessness = abs(magnitude - 1.055)
      smoothed = 0.9 * smoothed + 0.1 * restlessness
      limited = min(smoothed, 1.0)
      print(limited)

      # Pause for readability
      utime.sleep(0.1)

      # Read gyroscope data
      # gx, gy, gz = read_gyroscope()
      # print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))

      # Pause before the next set of readings
      # utime.sleep(0.05)

# Run the main function
if __name__ == "__main__":
   main()