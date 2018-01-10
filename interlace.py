a=int(input("enter the first number"))
b=int(input("enter the second number"))
eve=[]
odd=[]
for i in range(a,b):
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)
eve_count=eve.__len__()
odd_count=odd.__len__()
eve.reverse()
num=[]
range_num=b-a
j=0
k=0
while a<=b:
   while j<odd_count:
       num.append(odd[j])
       j=j+1
       a=a+1
       break
    while k<eve_count:
        num.append(eve[k])
        k=k+1
        a=a+1
        break
    
print num
    
