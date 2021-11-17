import os
import numpy as np
import cv2
import matplotlib.pyplot as plt 
import pickle

dir='D:\\web\\Images'
data=[]
genders=['male','female']
for gender in genders:
    path=os.path.join(dir,gender)
    label=genders.index(gender)
    for img in os.listdir(path):
        imgpath=os.path.join(path,img)
        imagesGender=cv2.imread(imgpath,0)
        try:
            imagesGender=cv2.resize(imagesGender,(50,50))
            image=np.array(imagesGender).flatten()
            data.append([image,label])
        except Exception as e:
            pass

pick_in=open('data1.pickle','wb')
pickle.dump(data,pick_in)
pick_in.close()
        
    
