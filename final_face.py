from itertools import count

import time
import ardconnect

import cv2  # cv is a library designed to solve computer vision problems like face detection
import numpy as np  # helps in calculations of arrays and matrices
import face_recognition  # used to locate and visualize the human faces
import os  # provides functions for interacting with the operating system
from datetime import datetime # supplies classes for manipulating date and time
import sqlite3
import time 

cur_time=time.time()
file1=open("dosage.txt","w")
path = 'images'
images = []
classNames = []
myList = os.listdir(path)  # to grab the list of images from the folder(in the form of name.jpg)

count = 0

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}') # imread function comes with open cv
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0]) # splits and takes the first element that is the name without jpeg
print(classNames)# gives the names without the jpg format


def findEncodings(images):
    encodeList = []  # this list will have all the encodings at the end
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert BGR to RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode) #does the encodings and append it to the list
    return encodeList


encodeListKnown = findEncodings(images)
print('encoding complete')

def display(id):
        global count
    
        conn=sqlite3.connect("FaseBase.db")
        cmd="SELECT * FROM patient WHERE ID="+str(id)
        cursor=conn.execute(cmd)
        profile=None
        for row in cursor :
            profile=row
            count+=1
        conn.close()
        #if(time.time()>cur_time+50):
        print("success")
        file1.write(str(profile[6]))
        file1.close()
            



        print(profile)
        return profile








#encodeListKnown = findEncodings(images)
#print('encoding complete')

cap = cv2.VideoCapture(0) # initialize the webcam #
cur_time=time.time()
while True:
    
    
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25) # reduces size of image to speed up the process
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis) # compares the images and the encodings
        matchIndex = np.argmin(faceDis) # gives the encodings of the max matching face
        y1,x2,y2,x1 = faceLoc
        y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

        if matches[matchIndex]:
            name = str(classNames[matchIndex])
            print(name)
            #y1,x2,y2,x1 = faceLoc
            #y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            
            
            profile=display(matchIndex)
            
                
            
            if(profile!=None):
                    
                cv2.putText(img,str(profile[1]),(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2) # to make a box around the face and display the name of the image
                cv2.putText(img,str(profile[2]),(x1+6,y2-6+30),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                cv2.putText(img,str(profile[3]),(x1+6,y2-6+60),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                cv2.putText(img,str(profile[4]),(x1+6,y2-6+90),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                #if(time.time()<cur_time+5):
                #    cap.release()
                 #   cv2.destroyAllWindows()

            

            else:
            
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, 'Face Not Found', (x1 + 6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 2)





    cv2.imshow('Webcam',img)
    if(cv2.waitKey(0) & 0xFF == ord('q')):
        break



ardconnect.compile()

    
    