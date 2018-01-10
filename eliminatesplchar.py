def eliminate_spl_char(str): 
    n=len(str)
    str=str.lower()
    nstr=''
    s=''
    for i in range(n):
        if str.rindex(i)=='a' or str.rindex(i)=='b' or str.rindex(i)=='c' or str.rindex(i)=='d' or str.rindex(i)=='e' or str.rindex(i)=='f' or str.rindex(i)=='g' or str.rindex(i)=='h' or str.rindex(i)=='i' or str.rindex(i)=='j' or str.rindex(i)=='k' or str.rindex(i)=='l' or str.rindex(i)=='m' or str.rindex(i)=='n' or str.rindex(i)=='o' or str.rindex(i)=='p' or str.rindex(i)=='q' or str.rindex(i)=='r' or str.rindex(i)=='s' or str.rindex(i)=='t' or str.rindex(i)=='u' or str.rindex(i)=='v' or str.rindex(i)=='w' or str.rindex(i)=='x' or str.rindex(i)=='y' or str.rindex(i)=='z':
            nstr=str.rindex(i)
    return nstr

str=input('enter a string')
str1=eliminate_spl_char(str)
print str1

            
    
