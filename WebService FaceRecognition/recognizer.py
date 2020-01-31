import os
import numpy as np
from PIL import Image
import cv2
import pickle

#Change PATHS to YOUR path

#Training DATA Directory
directory = '/home/AymanKoOo/mysite/Students'
#############################################

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 1
label_ids = {}
y_labels = []
x_train = []

##Enters inside root dir file
for root,dirs,files in os.walk(directory):
    for file in files:
        if file.endswith("PNG") or file.endswith("jpg"):
          #print Image path
          path = os.path.join(root,file)#7ot 3lehom al root we file
          label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()#name of the folder mohamed salah
          print(label,path)

        ##Giving id to a label
          if not label in label_ids:
              label_ids[label]=current_id  #key is label and value is the id
              current_id+=1

          id_ = label_ids[label]

          ##Converts Image into Pixels array##
          pil_image = Image.open(path).convert("L")#grayscale



          image_array = np.array(pil_image,"uint8")
          faces = face_cascade.detectMultiScale(image_array, scaleFactor = 1.3, minNeighbors=5)

          for x,y,w,h in faces:
            roi = image_array[y:y+h,x:x+w]
            x_train.append(roi)
            y_labels.append(id_)

print(y_labels)
with open("labels.pickle",'wb') as f:
    pickle.dump(label_ids,f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save('/home/AymanKoOo/mysite/trainingData.yml')