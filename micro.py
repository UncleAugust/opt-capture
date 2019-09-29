import speech_recognition as sr
import cv2
import serial
r = sr.Recognizer()
with sr.Microphone() as source:
    print("говори")
    audio = r.listen(source,timeout=7)
try:
    print("[СКАЗАЛ]: " + r.recognize_google(audio, language='RU-ru').lower())
    if r.recognize_google(audio, language='RU-ru').lower().find('дай') != -1 :
        print("Отправка в сериал")
        ser = serial.Serial("COM7", 9600)
        while True:
            ser.write(b"h")
            print('ОТПРАВЛЕНО')
except sr.WaitTimeoutError:
    print('Разрыв по тайм-аут`у')
except sr.UnknownValueError:
    print("не понимаю тебя")
except sr.RequestError as e:
    print("Нет обратки с гугла {0}".format(e))
