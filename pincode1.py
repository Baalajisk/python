import csv
with open("C:\Users\Admin\Downloads\pin.csv") as csvfile:
    read=csv.DictReader(csvfile)
    key=raw_input("enter the first 5 letters of the place ")
    for i in read:
        string=str(i['officename'])
        if string.__getslice__(0,5)==key:
            print(i['officename'],i['pincode'])
