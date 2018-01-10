'''
Created on Apr 22, 2017
THE PROGRAM WILL ENCODE THE CONSONANTS IN THE STRING
@author: Admin
'''
def check_consonants(str1):
    ls=list(str1)
    len=ls.__len__()
    s=''
    for i in range(len):
        if ls[i]!='a' and ls[i]!='e' and ls[i]!='i' and ls[i]!='o' and ls[i]!='u':
            s=s+ls[i]+'o'+ls[i]
        else:
            s=s+ls[i]
    return s 
str1=raw_input("enter a string:")
cons=check_consonants(str1)
print cons