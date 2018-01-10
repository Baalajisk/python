s=input()
sl=list(s)
l=[]
for i in sl:
    l.append(int(i))
l.sort()
d={}
for i in l:
    if i not in d.keys():
        d[i]=l.count(i)
v=[]
k=[]
for i in d.keys():
    k.append(i)
for i in d.values():
    v.append(i)
k.sort()
v.sort()
v.reverse()
for j in v:
    for i in k:
        if j==d[i]:
            count=j
            while(count>0):
                print(i,end='')
                count=count-1
            k.remove(i)
            break
    
