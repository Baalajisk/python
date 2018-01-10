import tkinter as tk
from PIL import ImageTk,Image
import sqlite3
conn=sqlite3.connect('create.db')
c=conn.cursor()
'''c.execute("CREATE TABLE user(name CHAR(20),email CHAR(50))")'''
def insert():
    n=e1.get()
    e=e2.get()
    c.execute("INSERT INTO user(name,email)VALUES('%s','%s')"%(n,e))
    conn.commit()
    root.destroy()
    c.execute("SELECT * FROM user")
    print(c.fetchall())
    
    
    
    
root=tk.Tk()
root.geometry('1600x900')
root.title('login form')
path='C:\\Users\\Admin\\Desktop\\usainbolt.jpg'
img=ImageTk.PhotoImage(Image.open(path))
panel=tk.Label(root,image=img)
panel.pack()
e1=tk.Entry(root)
e1.place(x=1200,y=150)
e2=tk.Entry(root)
e2.place(x=1200,y=300)
b1=tk.Button(root,text='create',command=insert)
b1.place(x=1000,y=400)
root.mainloop()


