from imageai.Detection import ObjectDetection
import os
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\models\\resnet50_coco_best_v2.0.1.h5"))
detector.loadModel() ## NOTE: 1 секунда, 5 объектов, самое быстрое для распознавания.
print('LOADED')
print('LOADED2')

detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\project\\images\\kh.jpg"), output_image_path=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\iimg1.jpg"))
print('=================================IMG 1=================================')
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
