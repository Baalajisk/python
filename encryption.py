from PIL import Image
import sys
import os
import random
import secrets
import tkinter
from tkinter import *
def encrypt():
       cel=[]
       dec=[]
       ff=[]
       flagc=0
       n=int(input('Enter the number of temperature'))
       if(int(n%10)==int(n)):
              nn='00'+str(n)
       elif(int(n/100)==int(0)):
              nn='0'+str(n)
       crad=secrets.choice(range(0,200))
       drad=secrets.choice(range(0,200))
       #gui code starts
         
       cc=StringVar()
       l1=Label(t,text='enter the color for celsius').grid(row=1,column=1)
       e1=Entry(t,textvariable=cc).grid(row=1,column=2)
       fc=StringVar()
       l2=Label(t,text='enter the color for decimal').grid(row=2,column=1)
       e2=Entry(t,textvariable=fc).grid(row=2,column=2)
       dc=StringVar()
       l3=Label(t,text='enter the color for random number').grid(row=3,column=1)
       e3=Entry(t,textvariable=dc).grid(row=3,column=2)
       c=StringVar()
       for i in range(0,n):
           l4=Label(t,text("enter the value for c")).grid(row=4,column=1)   
           e4=Entry(t,textvarible=c).grid(row=4,column=2)   
           c=float(c)
           if c<0:
               c=float(c*-1)+100
               flagc=1
           d=((float(c)*100)%100)
           c=int(c)+crad
           d=int(d)+drad
           f=secrets.choice(range(0,255))    
           cel.append(c)
           dec.append(d)
           ff.append(f)
       root=StringVar()    
       l4=Label(t,text="Enter the path").grid(row=5,column=1)
       
       file_name=input("Enter the file name")
       aa=int(input("Enter the first location"))
       if(int(aa/10)==int(0)):
              aaa='0'+str(aa)
       ab=int(input("Enter second location"))
       if(int(ab/10)==int(0)):
              abb='0'+str(ab)
       pic =Image.open(os.path.join(root, file_name))
       choice=int(input("1.Diagonal or 2.Vertical or 3.Horizontal"))
       for i in range(0,n):
           if(cc=='R' or cc=='r'):
               x=cel[i]
               kc=1
           elif(cc=='G' or cc=='g'):
               y=cel[i]
               kc=2
           elif(cc=='B' or cc=='b'):
               z=cel[i]
               kc=3
           if(fc=='R' or fc=='r'):
               x=ff[i]
               kf=1
           elif(fc=='G' or fc=='g'):
               y=ff[i]
               kf=2
           elif(fc=='B' or fc=='b'):
               z=ff[i]
               kf=3
           if(dc=='R' or dc=='r'):
               x=dec[i]
               kd=1
           elif(dc=='G' or dc=='g'):
               y=dec[i]
               kd=2
           elif(dc=='B' or dc=='b'):
               z=dec[i]
               kd=3
           pic.putpixel((int(aa),int(ab)),(int(x),int(y),int(z)))
           if(int(choice)==int(1)):
               aa=int(aa)+1
               ab=int(ab)+1
           elif((int(choice)==int(2))):
               ab=ab+1
           elif((int(choice)==int(3))):
               aa=aa+1    
       if(int(crad%10)==int(crad)):
              crad='00'+str(crad)
       elif(int(crad/100)==int(0)):
              crad='0'+str(crad)
       if(int(drad%10)==int(drad)):
              drad='00'+str(drad)
       elif(int(drad/100)==int(0)):
              drad='0'+str(drad)
       outpath=input("Enter the path")
       outname=input("Enter the file name")
       fileformat=input('Enter the file format with dot in front')
       outname=str(outname+fileformat)
       pic.save(os.path.join(outpath, outname))
       key=((str(nn)+str(crad)+str(drad)+str(random.randrange(0,9,2))+str(flagc)+str(random.randrange(0,9,2))+str(kc)+str(kd)+str(choice)+str(aaa)+str(abb)))
       print(key)
t=Tk()
t.title("ENCRYPTION")
t.configure(bg='yellow')
t.geometry('750x750')
l1=Label(t,text=
