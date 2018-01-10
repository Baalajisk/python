str=input("enter the string")
a=len(str)
l=[]
for i in range(0,len(str)):
    for j in range(0, i):
            s= str[j:i + 1]
            if s not in l:
                l.append(s)
nl=[]
for i in l:
    if(i==i[::-1]):
        nl.append(i)
count=0
for i in nl:
    if(len(i)>count):
       count=len(i)
       ns=i
print(ns)
