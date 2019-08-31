
#from imageai.Detection import VideoObjectDetection
#import os

#execution_path = os.getcwd()

#detector = VideoObjectDetection()
#detector.setModelTypeAsYOLOv3()
#detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\yolo.h5"))
#detector.loadModel()

#video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "C:\\Users\\Admin_Robo\\Desktop\\20190830_151839.mp4"),
#                                output_file_path=os.path.join(execution_path, "traffic_mini_detected_1")
#                                , frames_per_second=1, log_progress=True)
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

detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\img1.jpg"), output_image_path=os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\iimg1.jpg"))

print('=================================IMG 1=================================')
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
