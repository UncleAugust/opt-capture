import serial
ser = serial.Serial('COM5', 115800)
print(ser.name)
ser.write(b'c')
