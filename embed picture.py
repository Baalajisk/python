import tkinter as tk
from PIL import ImageTk,Image
import sqlite3




def show():
    p1=tk.Tk()
    p1.title('kokrajhar')
    p1.geometry('500x500')
    b1=tk.Button(p1,text='add case',fg='red',command=place1).pack()
    p1.mainloop()

def place1():
    conn=sqlite3.connect('example.db')
    c=conn.cursor()
    case=0
    c.execute("UPDATE districts SET crime=? WHERE name='kokrajhar'",1)
    


window=tk.Tk()
window.title('assam_map')
window.geometry('1600x900')
path="C:\\Users\\Admin\\Desktop\\AssamDistricts.jpg"
img=ImageTk.PhotoImage(Image.open(path))
panel=tk.Label(window,image=img)
panel.pack()
v=tk.IntVar()
r1=tk.Radiobutton(window,value=1,variable=v,command=show).place(x=456,y=231)



    
    


                        
