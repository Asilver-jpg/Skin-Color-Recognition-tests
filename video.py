import cv2
import sys
import os
import random
import time
#create an array of strings. Each index is the name of a different video you want to play.
def videoArr():
    colArr=[0 for x in range(4)]
    colArr[0]= "blue.MP4"
    colArr[1]= "green (1).MP4"
    colArr[2]= "pink.MP4"
    colArr[3]= "white.MP4"
    return colArr
#get the string from a random index in the array
def randomVideo(colArr):
    rand= random.randint(0,2)
    answer= colArr[rand]
    return answer
#plays a video, make sure default video player is VLC
def videoPlay(str):
    try:
        os.startfile(str)
    except Exception, e:
        print str(e)
#closes VLC
def closeVideo():
    try:
        os.system('TASKKILL /F /IM VLC.exe')
    except Exception, e:
        print str(e)


colArr= videoArr()
play=False
playing=False;
#cascade for face finding
faceCascade = cv2.CascadeClassifier('C:\Program Files\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
startTime=0
repeat=False
#video capture from webcam
video_capture = cv2.VideoCapture(0)
count=0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect if there are faces, store in 3D array
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    #turn on white video if no face prescence in the beginning
    if(faces==() and playing==False):
        videoPlay(colArr[3])
        playing=True
    #if there is  face found, play a random video based on a random string from array.
    if(faces !=() and play==False ):
        video=randomVideo(colArr)
        videoPlay(video)
        play=True
    #play white video if no face found
    elif(faces==() and play==True):

        videoPlay(colArr[3])
        play=False;
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
#video_capture.release()
#cv2.destroyAllWindows()
input('Press ENTER to exit')
