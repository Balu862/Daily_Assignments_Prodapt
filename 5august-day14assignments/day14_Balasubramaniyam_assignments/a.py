import csv,json,requests
f=open('petrol1.json')
data=json.load(f)
for i in data:
    if float(i['rate'])<70:
        print(i)