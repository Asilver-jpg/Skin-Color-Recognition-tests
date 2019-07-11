import cv2
import numpy as np
import colorCalc as col

img = cv2.imread('face.jpg', -1)


face_cascade = cv2.CascadeClassifier('C:\Program Files\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\Program Files\opencv\sources\data\haarcascades\haarcascade_eye.xml')


rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)
cv2.imwrite('result.png', result)
result= cv2.imread('result.png')
gray = cv2.imread('result.jpg',0)



faces = face_cascade.detectMultiScale(gray, 1.3, 5)
x1= faces[0][0]
x2= faces[0][2]
y1= faces[0][1]
y2= faces[0][3]

for (x,y,w,h) in faces:
    result = cv2.rectangle(result,(x,y),(x+w,y+h),(255,0,0),2)
    gray= cv2.rectangle(gray,(x,y),(x+w,y+h),(0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = result[y:y+h, x:x+w]


array= col.colorArray();
height, width = result.shape[0],result.shape[1]

sl= result[x1:x1+x2,y1:y1+y2]
#print(col.colorAnswerRange(sl))

cv2.destroyAllWindows()


cv2.imshow('result',img)

input('Press ENTER to exit')
