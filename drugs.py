import tkinter as tk
from PIL import ImageTk,Image
import sqlite3
conn=sqlite3.connect('drugs.db')
c=conn.cursor()
def password_check():
    if e6.get()==e7.get():
        
        signup()
    else:
        msg=tk.Message(login,text='password should be same')
        msg.place(x=1300,y=435)
def signup():
    '''c.execute("CREATE TABLE signup(pharmacy_name CHAR(30),password CHAR(30),location CHAR(30))")'''
    pname=e5.get()
    pas=e6.get()
    loc=e8.get()
    login.destroy()
    c.execute("INSERT INTO signup(pharmacy_name,password,location)VALUES('%s','%s','%s')"%(pname,pas,loc))
    conn.commit()

def log_in():
    global pname
    pname=e1.get()
    pas=c.execute("SELECT password FROM signup WHERE pharmacy_name=='%s'"%(pname))
    pas1=c.fetchone()
    pwrd=str(e2.get())
    if pwrd in pas1:
        login.destroy()
        firstpage()
        
        
    else:
        msg1=tk.Message(login,text='password does not matches')
        msg1.place(x=1275,y=85)
def firstpage():
    first=tk.Tk()
    first.geometry('1600x900')
    first.title('firstpage')
    path1='C:\\Users\\Admin\\Desktop\\medicine1.jpg'
    img1=ImageTk.PhotoImage(Image.open(path1))
    panel1=tk.Label(first,image=img1)
    panel1.pack(fill='both')
    global e9
    e9=tk.Entry(first)
    e9.place(x=700,y=400)
    global e10
    e10=tk.Entry(first)
    e10.place(x=700,y=550)
    b=tk.Button(first,text='submit',command=medicine_info)
    b.place(x=700,y=600)
    first.mainloop()
def medicine_info():
    '''c.execute("CREATE TABLE medicine_info(pharmacy_name CHAR(30),medicine CHAR(30),salt CHAR(30))")'''
    '''c.execute("DROP TABLE medicine_info")'''
    
    m=e9.get()
    s=e10.get()
    '''print(pname)
    print(m)
    print(s)'''
    c.execute("INSERT INTO medicine_info(pharmacy_name,medicine,salt)VALUES('%s','%s','%s')"%(pname,m,s))
    conn.commit()
    
login=tk.Tk()
login.geometry('1600x900')
login.title('login')
path='C:\\Users\\Admin\\Desktop\\health.jpg'
img=ImageTk.PhotoImage(Image.open(path))
panel=tk.Label(login,image=img)
panel.pack()
e1=tk.Entry(login)
e1.place(x=975,y=65)
global pn
pn=e1.get()
print(pn)
e2=tk.Entry(login)
e2.place(x=1275,y=65)
e3=tk.Entry(login)
e3.place(x=300,y=230)
e4=tk.Entry(login)
e4.place(x=300,y=310)
e5=tk.Entry(login)
e5.place(x=1200,y=300)
e6=tk.Entry(login) 
e6.place(x=1200,y=370)
e7=tk.Entry(login)
e7.place(x=1200,y=435)
e8=tk.Entry(login)
e8.place(x=1200,y=510)
b1=tk.Button(login,text='login',command=log_in)
b1.place(x=1200,y=100)
b2=tk.Button(login,text='search')
b2.place(x=300,y=350)
b3=tk.Button(login,text='create',command=password_check)
b3.place(x=1200,y=550)
login.mainloop()
