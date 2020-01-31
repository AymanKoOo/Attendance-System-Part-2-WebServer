import cv2
import pickle
import numpy as np
from DataBasse import database
import random
from datetime import datetime

def process(enImg):

                now = datetime.now() # current date and time
                date_time = now.strftime("%m/%d/%Y")
                ####
                ob=database()
                #decode enImg into real img#
                nparr = np.fromstring(enImg, np.uint8)
                imgg = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
                #############################
                effective_but_smaller_size = (640, 480)  # or whatever you find works
                img = cv2.resize(imgg, effective_but_smaller_size, interpolation=cv2.INTER_AREA)
                #OpenCV operations#
                face_cascade = cv2.CascadeClassifier('/home/AymanKoOo/mysite/haarcascade_frontalface_default.xml')
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                recognizer.read('/home/AymanKoOo/mysite/trainingData.yml')
                #Converts img into gray scale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)
                ##################################################################

                for x,y,w,h in faces:
                   presentID=random.randint(1500, 100000)#random id
                   #cv2.rectangle(imgg, cv2.COLOR_BGR2GRAY, (x,y), (x+w,y+h), (255,0,0),3)
                   id_, conf = recognizer.predict(gray[y:y+h,x:x+w])  #Our trained model is working here
                   ob.insert_AttendanceData(presentID,id_,1,date_time)






