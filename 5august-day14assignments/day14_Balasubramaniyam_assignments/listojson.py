import json

student=[{"Name":"Balu","age":1},{"Name":"Dhoni","age":7}]

jsondata=json.dumps(student)

with open("newjson.json","w+",encoding="utf-8") as newj:
    newj.write(jsondata)