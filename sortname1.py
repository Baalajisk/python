"""sorting the names"""
lists=[]
limit=input("enter the range")
for i in range(limit):
    lists.insert(i,input("enter the name"))
lists.sort()
for i in range(limit):
    print lists[i]
                 


