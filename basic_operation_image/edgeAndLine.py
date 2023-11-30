import cv2
import numpy as np

img = cv2.imread('/home/swornimstha/Desktop/backup/backups/python/opencv/assets/line.jpg')
img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)
cv2.imshow('image',img)
edge = cv2.Canny(img,75,150)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lines = cv2.HoughLinesP(edge,1,np.pi/180,150)
cv2.imshow('image',gray)
# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imshow("lines",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if lines is not None:
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow("lines",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No lines detected")
