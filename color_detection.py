import cv2
import numpy as np
from collections import Counter

file_path='/home/umar/ML-AI/OpenCV-Projects/Background-color-detector/picture2.jpg'

def find_background(path=None):
    if(path is not None):
        img=cv2.imread(path)
        img=cv2.resize(img,(800,600))

        blue,green,red=cv2.split(img)
        blue=blue.flatten()
        green=green.flatten()
        red=red.flatten()   

        blue_counter=Counter(blue)
        green_counter=Counter(green)
        red_counter=Counter(red)

        blue_most=blue_counter.most_common(10)
        blue_avg=[i for i,j in blue_most]
        blue_avg=int(np.mean(blue_avg))

        green_most=green_counter.most_common(10)
        green_avg=[i for i,j in green_most]
        green_avg=int(np.mean(green_avg))

        red_most=red_counter.most_common(10)
        red_avg=[i for i,j in red_most]
        red_avg=int(np.mean(red_avg))


        background=[blue_avg,green_avg,red_avg]

        bg=np.zeros((512,512,3),np.uint8)
        bg_color=cv2.rectangle(bg,(0,0),(512,512),background,-1)

        return(bg_color)

    else: 
        return(None)


#print(background)
bg_image=find_background(file_path)

#cv2.imshow('Image',img)
cv2.imshow('Background',bg_image)

cv2.waitKey(0)
cv2.destroyAllWindows()