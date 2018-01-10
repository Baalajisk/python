import tkinter
import sqlite3
def addStock():
    root = Tk()
    root.title('Add Stock')
    label1 = Label(root, text='Gender')
    label2 = Label(root, text='Price')
    label3 = Label(root, text='Enter Product Name')
    label4 = Label(root, text='Colour')
    label5 = Label(root, text='Size')
    label6 = Label(root, text='Enter Amount')
    label7 = Label(root, text='Source')
    label8 = Label(root, text='Enter ProductID')
    entry1 = Entry(root)
    entry2 = Entry(root)
    entry3 = Entry(root)
    entry4 = Entry(root)
    entry5 = Entry(root)
    entry6 = Entry(root)
    entry7 = Entry(root)
    entry8 = Entry(root)

    label1.grid(row=0, sticky=E)
    label2.grid(row=1, sticky=E)
    label3.grid(row=2, sticky=E)
    label4.grid(row=3, sticky=E)
    label5.grid(row=4, sticky=E)
    label6.grid(row=5, sticky=E)
    label7.grid(row=6, sticky=E)
    label8.grid(row=7, sticky=E)

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    entry6.grid(row=5, column=1)
    entry7.grid(row=6, column=1)
    entry8.grid(row=7, column=1)

    frame3 = Frame(root)
    frame3.grid(columnspan = 2)

    button1 = Button(frame3, padx=10, pady=10, bd=2, text="Add Stock", command=insert_data)
    button1.pack()
def insert_data(values): 
    with sqlite3.connect("jam_stock.db") as db:
        cursor = db.cursor()
        sql = "insert or ignore into Product (Name, ProductID) values (?,?)"
        query(sql,values)
        db.commit()

def insert_product_type_data(records): #normalised
    sql = "insert into ProductType(AmountInStock, Size, Colour, Source) values (?,?,?,?)"
    for record in records:
        cursor.execute(sql,record)

def insert_product_gender_data(records): #normalised
    sql = "insert into ProductGender(Gender, Price) values (?,?)"
    for record in records:
        cursor.execute(sql, records)
