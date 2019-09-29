
#from imageai.Detection import VideoObjectDetection
#import os

#execution_path = os.getcwd()

#detector = VideoObjectDetection()
#detector.setModelTypeAsYOLOv3()
#detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\yolo.h5"))
#detector.loadModel(detection_speed='faster')

#video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "C:\\Users\\Admin_Robo\\Desktop\\WIN_20190912_17_36_23_Pro.mp4"),
    #                            output_file_path=os.path.join(execution_path, "C:\\Users\\Admin_Robo\\Desktop\\esp_test")
    #                            , frames_per_second=29, log_progress=True)
#print(video_path)

from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\resnet50_coco_best_v2.0.1.h5"))
detector.loadModel(detection_speed='faster') ## NOTE: 1 секунда, 5 объектов, самое быстрое для распознавания.
print('LOADED')
print('LOADED2')

detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\WIN_20190919_18_18_19_Pro.jpg"), output_image_path=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\iimg666.jpg"))

print('=================================IMG 1=================================')
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
