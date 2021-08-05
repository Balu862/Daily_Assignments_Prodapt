import csv,json

csvsource="diesel.csv"

dieselist=[]
with open(csvsource,'r',encoding="utf-8") as fs:
    data=csv.reader(fs)
    print(data)
    for i in data:
        dieselist.append(i)
dieseltojson=json.dumps(dieselist)
print(dieseltojson)
with open('diesel.json','w+',encoding="utf-8") as f1:
    f1.write(dieseltojson)
