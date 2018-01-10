"""pincode to area"""
import csv
with open("C:\Users\Admin\Downloads\pin.csv") as csvfile:
    d_reader=csv.DictReader(csvfile)
    pin=str(input('enter the pincode'))
    for row in d_reader:
        if row['pincode']==pin:
            print(row['officename'],row['pincode'])
