import tkinter
from tkinter import *
def printnum():
    x=a.get()
    l1=Label(t,text=x).grid(row=4,column=4)
    return
t=Tk()
a=IntVar()
l=Label(t,text='enter the number').grid(row=1,column=1)
e=Entry(t,textvariable=a).grid(row=2,column=2)
b=Button(t,text='print',command=printnum).grid(row=3,column=3)
