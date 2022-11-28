import json

with open("data.json") as file:
    data = json.load(file)

i = 0
while i<len(data):
    for k,v in data[i].items():
        print(k,":",v)
    print()
    i+=1