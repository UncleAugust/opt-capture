import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#while(True):
    # Capture frame-by-frame
ret, frame = cap.read()
    # do what you want with frame
    #  and then save to file
cv2.imwrite('C:\\Users\\Admin_Robo\\Desktop\\project\\test.png', frame)
#if cv2.waitKey(30) & 0xFF == ord('q'): # you can increase delay to 2 seconds here
#    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
