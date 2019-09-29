import serial
import time

ser = serial.Serial('COM7',9600)  # open first serial port
print(ser.portstr)
while True:
    ser.write(b"d")
