import cv2

img = cv2.imread('/home/swornimstha/Desktop/backup/backups/python/opencv/assets/download.png')

img = cv2.resize(img,(0,0),fx = 2,fy = 2)#to resize the window
# img = cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('/home/swornimstha/Desktop/backup/backups/python/opencv/nba.jpg',img)
import cv2 as cv

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()