s=int(input())
e=int(input())
l=list(range(s,e+1))
lt=len(l)
count=0
while count<lt-1:
    i=0
    while i<=count:
        print(s,end='')
        i=i+1
    temp_list=l[count+1:]
    for a in temp_list:
        print(a,end='')
    print()
    count=count+1
n=count
i=0
while i<n-1:
    j=0
    while j<count-1:
        print(s,end='')
        j=j+1
    while j<=n:
        print(e,end='')
        j=j+1
    print()
    i=i+1
    count=count-1
    
    
