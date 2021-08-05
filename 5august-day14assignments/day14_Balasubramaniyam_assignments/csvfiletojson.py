import json,csv
csvsource="studentsource.csv"

studentlist=[]
with open(csvsource,'r') as fi:
    datareader=csv.DictReader(fi)
    for i in datareader:
        studentlist.append(i)

jsonconverteed=json.dumps(studentlist)
print(jsonconverteed)
with open('newjson1.json','w',encoding="utf-8") as f1:
    f1.write(jsonconverteed)