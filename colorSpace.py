import cv2 as cv 
import numpy as np

img= cv.imread('face.jpg')

hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
print("OK")
cv.imshow('face', img)