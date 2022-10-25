import cv2
import numpy as np

def yazdir(histogram):
    for k in range (0,256):
        print(k,"=",histogram[k])

photo=cv2.imread("image.png",0)


histogram= np.zeros(256)
[h,w]=np.shape(photo)
for i in range (0,h):
    for j in range (0,w):
        k=photo[i,j]
        histogram[k]=histogram[k]+1

yazdir(histogram)
cv2.imshow("image",photo)
cv2.waitKey()