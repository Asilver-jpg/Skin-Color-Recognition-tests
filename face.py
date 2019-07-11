import numpy as np
import cv2 as cv
import math
import colorCalc as col

#load xml files
face_cascade = cv.CascadeClassifier('C:\Program Files\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\Program Files\opencv\sources\data\haarcascades\haarcascade_eye.xml')

#define image and convert to grayscale
pic= cv.imread('meWebcam.jpg')

gray = cv.imread('meWebcam.jpg',0)
#Did this cause i accidentally wrote img instead of pic and im lazy for now
img= pic
color = np.array([])

#scan for faces and draw rectangle
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
x1= faces[0][0]
x2= faces[0][2]
y1= faces[0][1]
y2= faces[0][3]

lower= np.array([32,55,61])
upper= np.array([255,255,255])

#Tried using masks, a bit too complicated for what I am trying to do
#mask= cv.inRange(img, lower, upper)
#res= cv.bitwise_and(img,img, mask=mask)

topRight= y1+y2
bottomLeft= x1+x2

sl= np.mean(img[x1:x1+x2,y1:y1+y2, :], axis=2)
print(sl[0][2])
# taking a slice of the image

#img[x1:x1+x2, y1:y1+y2, :]= (0,0,0);


#Non-working Attempt

#x_range= range(x1,topRight+1)
#y_range= range(y1,bottomLeft+1)
#color=np.mean(gray[x1:x1+x2, y1:y1+y2, :], axis=2)
#for x in x_range:
 #   for y in y_range:
  #      avgR=avgR+gray[x][y]
   #     counter= counter+1
#img[x1:x1+x2, y1:y1+y2, :]= [0,0,0]



#draws an ROI rectangle
for (x,y,w,h) in faces:
    img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    gray= cv.rectangle(gray,(x,y),(x+w,y+h),(0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

#colArr=col.colorArray()
#Testing the method below
#answer=col.colorCheck(colArr,source)
#print(answer)
#print(col.colorAnswerRange(sl))


#showing image. Close image to stop, then hit enter
cv.imshow('pic',pic)
cv.waitKey(0)
cv.destroyAllWindows()



input('Press ENTER to exit')
