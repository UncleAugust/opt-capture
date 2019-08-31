import speech_recognition as sr
import cv2
from serial import serial
ser = serial.Serial('COM3', 9600)
ser.write('101')
#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("говори")
#    audio = r.listen(source)
#try:
#    print("[СКАЗАЛ]: " + r.recognize_google(audio, language='RU-ru'))
#except sr.UnknownValueError:
#    print("не понимаю тебя")
#except sr.RequestError as e:
#    print("Нет обратки с гугла {0}".format(e))
