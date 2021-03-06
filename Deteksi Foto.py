import numpy as np
import cv2
from matplotlib import pyplot as ptl
import sys

wajah_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mata_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

img = cv2.imread('jefri.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
wajah = wajah_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in wajah :
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = img[y:y+h,x:x+w]
    mata = mata_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in mata :
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
cv2.imshow("gebetan",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
