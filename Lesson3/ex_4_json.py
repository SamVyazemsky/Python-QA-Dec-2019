import json

with open("ex_4.json", "r") as read_file:
    data = json.load(read_file)

# with open("ex_4_1.json", 'w') as write_file:
#     json.dump(data, write_file)

json_string = json.dumps(data)
print(json_string)
json_string = json.dumps(data, indent=4)
print(json_string)
