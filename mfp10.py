## NOTE: Исп. Библ: TensorFlow + Keras
# # NOTE: Модели из kaggle.com
# from imageai.Detection import ObjectDetection
# import os
# execution_path = os.getcwd() ## NOTE: Работая папка
#
# detector = ObjectDetection()
# detector.setModelTypeAsRetinaNet() ## NOTE: Установка модели в качестве.....
# detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\models\\resnet50_coco_best_v2.0.1.h5")) # NOTE: Модели загрузка
# detector.loadModel() ## NOTE: + Установка скорости.
# print('LOADED')
# print('LOADED2')
#
# detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\kj.jpg"), output_image_path=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\kj.jpg"))
# print('=================================IMG 1=================================')
# for eachObject in detections:
#     print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
#
import speech_recognition as sr
import cv2
import serial
import numpy as np
from imageai.Detection import ObjectDetection
import os
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet() ## NOTE: Установка модели в качестве.....
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\models\\resnet50_coco_best_v2.0.1.h5")) # NOTE: Модели загрузка
detector.loadModel() ## NOTE: + Установка скорости.
print('LOADED')
print('LOADED2')
cap = cv2.VideoCapture()
ret, frame = cap.read()
cv2.imwrite('C:\\Users\\Admin_Robo\\Desktop\\project\\images\\test.png', frame)
cap.release()
cv2.destroyAllWindows()
while True:
    ## NOTE: Обработка
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\images\\test.png"), output_image_path=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\images\\test.png"))
    ## NOTE: Вывод с фотки
    print('=================================IMG 1=================================')
    for eachObject in detections:
        eachObject["name"].join(l)
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
