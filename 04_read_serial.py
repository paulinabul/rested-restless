import serial

# Open the serial connection to the XIAO (adjust the port name if needed)
ser = serial.Serial("/dev/cu.usbmodem101", 115200, timeout=1)

while True:
    line = ser.readline()          # read one line, arrives as bytes
    text = line.decode().strip()   # convert bytes to text, remove line break and spaces
    try:
        value = float(text)        # convert text to a number
    except ValueError:
        continue                   # not a valid number: skip this round
    print(value)