s=input("enter the string: ")
l=list(s)
a=[]
i=0
while(i<len(l)):
    if l[i].isalpha():
        a.append(l[i])
    else:
        num=''
        while(l[i].isdigit()):
            num=num+l[i]
            i=i+1
        a.append(num)
        i=i-2
    i=i+1
print(a)
