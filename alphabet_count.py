s=raw_input("enter the string")
l=list(s)
le=l.__len__()
c=[]
a=[]
for i in range(0,le-1):
    while s.count(l[i])!=0:
        c.append(s.count(l[i]))
        a.append(l[i])
        s=s.replace(l[i],"")

lea=a.__len__()
for i in range(0,lea):
    print a[i]
    print c[i]
