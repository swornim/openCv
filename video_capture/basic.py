import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()#to read the frame..The Boolean value, ret, indicates whether the frame 
                           #was read successfully.If the frame was read successfully, ret is True, otherwise it is False.
    # image = np.zeros(frame.shape,np.uint8)#uint8 = unsigned integer of 8 bits
    # # print(image)
    edge = cv2.Canny(frame,75,150)
    line = cv2.HoughLinesP(edge,1,np.pi/180,50)
    cv2.imshow('image',line)#to

    if cv2.waitKey(1) == ord('q'):
        break# breaks is 'q' is taken as input
cap.release()
cv2.destroyAllWindows()