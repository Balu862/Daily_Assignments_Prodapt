import csv,json

csvsource="petrol.csv"

petrollist=[]
with open(csvsource,'r',encoding="utf-8") as fs:
    data=csv.DictReader(fs)
    print(data)
    for i in data:
        petrollist.append(i)
petroltojson=json.dumps(petrollist)

print(petroltojson)
with open('petrol1.json','w+',encoding="utf-8") as f1:
    f1.write(petroltojson)
