import cv2
import random
#random pixel color from row-100 to all columns
img = cv2.imread('/home/swornimstha/Desktop/backup/backups/python/opencv/assets/download.png')
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
#copy image
tag = img[10:50, 30:100]
img[51:70, 30:50] = tag

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
