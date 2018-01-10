s=input()
c=input()

c1=c[0]
c2=c[2]
d=-1

for i in range(0,len(s)):
    if s[i]==c1:
        for j in range(i+1,len(s)):
            d=d+1
            if s[j]==c2:
                a=d
            else:
                continue
    else:
        continue
c1=c[2]
c2=c[0]
d=-1
for i in range(0,len(s)):
    if s[i]==c1:
        for j in range(i+1,len(s)):
            d=d+1
            if s[j]==c2:
                b=d
            else:
                continue
    else:
        continue
if a>b:
    print(b)
else:
    print(a)
    
            
        
            
        
