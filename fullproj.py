#CL EYE CAM3 - 7 sek
#многострочные комменты - CTRL + /
import speech_recognition as sr
import cv2
import serial
import numpy as np
from imageai.Detection import ObjectDetection
import os
d=""
p=0
l=[]
# NOTE: ЗАГРУЗКА
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\models\\resnet50_coco_best_v2.0.1.h5"))
detector.loadModel() ## NOTE: Для детекта минимального [незначительного] объекта - режим стандарт (7 sek ;()
print('LOADED')
ser = serial.Serial("COM8", 9600)
print('SERIAL KAROCHE')
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("говори")
        audio = r.listen(source,timeout=7)
    try:
        print("[СКАЗАЛ]: " + r.recognize_google(audio, language='RU-ru').lower())
        if r.recognize_google(audio, language='RU-ru').lower().find('дай') != -1:
            print('It works! #1')
            if r.recognize_google(audio, language='RU-ru').lower().find('стакан') != -1:
                d="cup"
                break
            elif r.recognize_google(audio, language='RU-ru').lower().find('банан') != -1:
                d = "banan"
                break
            elif r.recognize_google(audio, language='RU-ru').lower().find('игрушк') != -1:
                d = "potted plant"
                break
            else:
                print('Объекта нет')
                continue

        else:
            print('Не найдено "Дай"')
            continue

    except sr.WaitTimeoutError:
        print('Разрыв по тайм-аут`у')
        continue
    except sr.UnknownValueError:
        print("не понимаю тебя")
        continue
    except sr.RequestError as e:
        print("Нет обратки с гугла {0}".format(e))
        continue

#############################################################
while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('C:\\Users\\Admin_Robo\\Desktop\\project\\images\\test.png', frame)
    cap.release()
    cv2.destroyAllWindows()
    ## NOTE: Обработка
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\images\\test.png"), output_image_path=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\images\\test.png"))
    ## NOTE: Вывод с фотки
    print('=================================IMG 1=================================')
    for eachObject in detections:
        l.append(str(eachObject["name"]))
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

    print(l)
    if d in l:
        print('Объект в наличии.')
        print('работа ардуинки')
        if (d=="cup" or d == "potted plant" or d == "banana"):
            for i in range(50): ## NOTE: Около 10 сигналов он кинет.
                ser.write(b"c") ## NOTE: Отправка плюсика на чашку и игрушку.
                print('ОТПРАВЛЕНО: [C] ' + d)
            break



    else:
        while True:
            ## NOTE: Завершить килл процесса отправки на сериал и обновить цикл поиска.
            ##################
            ## NOTE: Если ардуинка не нашла - отдает на вывод сканеру снова, посредством принятия сериала.
            for i in range(5):
                ser.write(b"h") ## NOTE: Отправка +угла.
                print('ОТПРАВЛЕНО: [H] ' + d) ## NOTE: Отправка .
            while True:
                if(ser.readline().find(b"d")!=-1):## NOTE: Дисаблит прогу на break+continue
                    print('PC принял сигнал d. Выведен из цикла на отправку.')
                    break
                print('Вывод на начало цикла на момент сканирования...')
            break
        continue
print('Конец работы!')
l=[]
