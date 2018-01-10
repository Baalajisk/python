l=[]#to get input
while True:
    i=input()
    if i!='EndOfInput':
        l.append(i)
    else:
        break
c=[]#course info
count=1
for i in range(0,len(l)):
    l[i]=l[i].split('~')
while l[count][0]!='Students':
    c.append(l[count])
    count=count+1
cid=[]#course id
count=count+1
for i in range(0,len(c)):
    cid.append(c[i][0])
st=[]#student info
while l[count][0]!='Grades':
    st.append(l[count])
    count=count+1
sid=[]#student id
for i in range(0,len(st)):
    sid.append(st[i][0])
sid.sort()
sd={}#student dict
for i in range(0,len(st)):
    sd[st[i][0]]=st[i][1]
count=count+1
g=[]#grade info
while count<len(l):
    g.append(l[count])
    count=count+1
d={}#first dict
gd={'A':10,'AB':9,'B':8,'BC':7,'C':6,'CD':5,'D':4}#grade dict
for i in g:
    d[i[0]]={}
for i in g:
    d[i[0]][i[3]]=gd[i[4]]
di={}
n=0
for i in cid:
    if i not in d.keys():
        d[i]={}
for i in sid:
    if i not in d[cid[0]].keys():
        d[cid[0]][i]=0
    if i not in d[cid[1]].keys():
        d[cid[1]][i]=0
for i in sid:
    if d[cid[0]][i]>0 and d[cid[1]][i]>0:
        di[i]=(d[cid[0]][i]+d[cid[1]][i])/2
    elif d[cid[0]][i]>0:
        
        di[i]=2*((d[cid[0]][i]+d[cid[1]][i])/2)
    elif d[cid[1]][i]>0:
        di[i]=2*((d[cid[0]][i]+d[cid[1]][i])/2)
    else:
        di[i]=0
   
for i in sid:
    print(i+'~'+sd[i]+'~'+str(di[i]),sep='')
    

    

    

