import json
x='[{"name": "keerthana","age":2, "language":"english"},{"name":"sathana","age":19}]'
y=json.loads(x)
for item in y:
    print(item['name'],item['age'])