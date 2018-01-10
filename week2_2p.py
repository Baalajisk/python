def depth(string):
    total=0
    inc=0
    dec=0
    count=0
    for i in string:
        if i=='(':
            inc=inc+1
            count=count+1
        elif i==')':
            dec=dec+1
            if inc==dec:
                if count>total:
                    total=count
                                  
                count=0
                inc=0
                dec=0
    print(total)
s=input("enter the string")
depth(s)


                
            
