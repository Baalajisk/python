s=input('enter the string')
if len(s)%2!=0:
    i=len(s)//2
    j=i
else:
    j=len(s)//2
    i=j-1
p=''
while i>=0 and j<=len(s):
    if s[i]==s[j]:
        p=s[i:j+1]
        i=i-1
        j=j+1
    else:
        break
print(p)
        
