import numpy as np
import cv2 as cv
img = cv.imread(r'/home/swornimstha/Desktop/backup/backups/python/opencv/assets/download.png')
px = img[100,100]
print( px)
print(img.shape)#gives output in format of (height, width , channels)
print(img[0])#gives pixel coordinate at first row
print(img[232][45:100])#45:100 - from 45 pixel to 100 pixel