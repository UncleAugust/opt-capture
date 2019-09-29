import serial
import time

ser = serial.Serial('COM8',9600)  # open first serial port
while True:
    print(ser.readline())
    if(ser.readline().find(b"d")!=-1):
        break
print('Prinyato')
