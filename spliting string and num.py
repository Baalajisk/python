s=input("enter a string with single quotes")
a=[]
num=''
for i in s:
    if i.isdigit():
        num=num+i
        continue
    else:
        a.append(num)
        num=''
        a.append(i)
while a.count('')>0:
    a.remove('')
a.remove(a[0])
a.remove(a[len(a)-1])

print(a)
    
