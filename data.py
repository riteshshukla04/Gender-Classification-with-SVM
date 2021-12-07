import os
import numpy as np
import cv2
import matplotlib.pyplot as plt 
import pickle

import numpy as np
import matplotlib.pyplot as plt

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

        
count_male=0
count_female=0  
for i in data:
    if i[1]==0:
        count_male+=1
    else:
        count_female+=1
print(count_male)
dataset={
    "male":count_male,
    "female":count_female

}
gender = list(dataset.keys())
values = list(dataset.values())
plt.bar(gender, values, color ='maroon',
        width = 0.4)
plt.show()



pick_in=open('data1.pickle','wb')
pickle.dump(data,pick_in)
pick_in.close()
    
