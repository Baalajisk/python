l=[]
while True:
    i=input()
    if i!='':
        l.append(i)
    else:
        break
first=[]
second=[]
half=len(l)//2
for i in range(0,half):
    first.append(l[i])
for j in range(half,len(l)):
    second.append(l[j])
for j in second:
    print(j)
for i in first:
    print(i)
    
