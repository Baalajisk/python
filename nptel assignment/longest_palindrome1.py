n=int(input())
s=input()
p=''
l=[]
for count in range(n,0,-1):
    for i in range(0,n):
        if i+count<=n:
            p=s[i:i+count]
            if p==p[::-1]:
                print(len(p))
                print(p)
                break
    if p==p[::-1]:
        break
            
        
        
                


            
        
    
        
        




       
