import sqlite3
conn=sqlite3.connect('drugs.db')
c=conn.cursor()
c.execute("SELECT * FROM medicine_info")
p=c.fetchall()

print(p)
print(p[0][0])





