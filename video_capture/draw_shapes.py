import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(type(cap))
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))#get width of frame
    height = int(cap.get(3))#get height of frame
    #to draw line
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),2)
    #              source,starting point,endpoint,color,thickness 
    #to write text
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img,'you are great',(320,height-20),font,4,(0,0,0),5)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) == ord('q'):
        break;
cv2.release()
cv2.destroyAllWindows()
