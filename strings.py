def remove_space(string):
    string=string.replace(" ","")
    return(string)

def change_to_list(str):
    l=list(str)
    return(l)


def count(li):
    co=li.count(li[0])
    re=li[0]
    while co>0:
        li=li.remove(re)
    print li

    

print"enter the string"
string=raw_input()
string=remove_space(string)
li=change_to_list(string)
print li
count(li)
    
