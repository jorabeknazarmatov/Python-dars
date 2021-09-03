import json
a=5
a_json=json.dumps(a,indent=5)
print(a_json)
laptop={
    "protsessor":'i-5',
    "pokoleniya": 9,
    "video": 4,
    "RAM": 8
    }
laptop_json=json.dumps(laptop,indent=4)
'''with open('laptop_json','w') as f:
    json.dump(laptop,f)
print(laptop_json)
'''
pc=json.loads(laptop_json)
print(pc)
