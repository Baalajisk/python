import tkinter
from tkinter import *
t=Tk()
variables=[]
entries=[]
for i in range(10):
    va=StringVar()
    en=Entry(t,textvariable=va).grid(row=1,column=i+1)
    variables.append(va)
    entries.append(en)
