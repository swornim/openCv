import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # low_yelow = np.array([18,94,140])
    # up_yellow = np.array([48,255,255])
    # mask = cv2.inRange(frame,low_yelow,up_yellow)
    edge = cv2.Canny(frame,75,150)
    lines = cv2.HoughLinesP(edge,1,np.pi/180,150)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if lines is not None:
        for line in lines:
            print(type(line[0]))
            # for HoughLinesP
            x1,y1,x2,y2 = line[0]
            # cv2.line(mask,(x1,y1),(x2,y2),(0,255,0),2)
            #"for HoughLines"
            # #This is because the HoughLines method returns an array of lines represented by rho and theta parameters, where rho is the distance from the origin to the line and theta is the angle in radians between the positive x-axis and the line.
            # rho, theta = line[0]
            # a = np.cos(theta)
            # b = np.sin(theta)             
            # x0 = a * rho
            # y0 = b * rho
            # x1 = int(x0 + 1000 * (-b))
            # y1 = int(y0 + 1000 * (a))
            # x2 = int(x0 - 1000 * (-b))
            # y2 = int(y0 - 1000 * (a))

            cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame',lines)
    # cv2.imshow('line',lines)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()