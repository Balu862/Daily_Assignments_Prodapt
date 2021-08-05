import json
with open("petrol1.json",'r') as petrolfile:
    data=petrolfile.read()
    da=json.loads(data)
    a=[print(i) for i in da if float(i['rate'])<70.00]

