def qsort(l,r,li):
    pivot=l
    for i in range(l+1,r):
        if li[pivot] <li[i]:
            break
    for j in range(r,l,-1):
        if li[pivot]>li[j]:
            break
    if i<j:
        temp=li[i]
        li[i]=li[j]
        li[j]=temp
    else:
        temp=li[pivot]
        li[pivot]=li[j]
        li[j]=temp
        qsort(0,j-1,li)
        qsort(j+1,r,li)
    
    
