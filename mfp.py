
from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "C:\\Users\\Admin_Robo\\Desktop\\yolo.h5"))
detector.loadModel(detection_speed='faster')

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "C:\\Users\\Admin_Robo\\Desktop\\WIN_20190912_17_36_23_Pro.mp4"),
                                output_file_path=os.path.join(execution_path, "C:\\Users\\Admin_Robo\\Desktop\\esp_test"), frames_per_second=1, log_progress=True)
print(video_path)
