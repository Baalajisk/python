import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk,Image
import time
from pygame import mixer
o=time.time()
o=str(o)
o=o+'.avi'
'''l=o.split(' ')
s='_'
for i in l:
    s=i+s
    
s=s+'.avi'
print(s)'''
mixer.init()
mixer.music.load('alarm.mp3')

fourcc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter(o,fourcc,20.0,(640,480))

def recognize():

    
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')


    cap=cv2.VideoCapture(0)

    a=time.time()

    face_count=0
    eye_count=0
    while True:
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.3, 5)
        out.write(img)
        
        
            
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
            roi_gray=gray[y:y+h, x:x+w]
            roi_color=img[y:y+h, x:x+w]
            eyes=eye_cascade.detectMultiScale(roi_gray)
            face_count+=1
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                eye_count+=1
        
        

        cv2.imshow('img',img)
        b=time.time()
        if (b-a)>15:
            mixer.music.play()
            
            
        if eye_count>=10 and face_count>=10:
            print("allow")
            out.release()
            eye_count=0
            face_count=0
            break
        k=cv2.waitKey(30) & 0xff
        if k==27:
            break

    cap.release()
    cv2.destroyAllWindows()
root=tk.Tk()
root.geometry('1600x900')
im=ImageTk.PhotoImage(Image.open('lock.jpg'))
panel=tk.Label(root,image=im)
panel.pack()
b1=tk.Button(root,text='recognize',command=recognize)
b1.place(x=750,y=350)
root.mainloop()
