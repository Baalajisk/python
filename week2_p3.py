import math
def sumsquares(l):
    sum=0
    for i in l:
        a=i**0.5
        b=int(i**0.5)
        c=a/b
        if c==1.0:
            sum=sum+i
    print(sum)
l1=input("enter a list")
sumsquares(l1)
