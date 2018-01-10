s=input()
n=input()
mlen=0
l=[]
for count in range(1,len(s)+1):
    i=0
    while i+count<=len(s):
        if s[i:i+count] not in l:
            l.append(s[i:i+count])
        i=i+1
p=[]
for i in l :
    if i==i[::-1]:
        p.append(i)
longp=''
for i in p:
    if len(i)>mlen:
        longp=i
print(longp)

    
    
    
    
    
