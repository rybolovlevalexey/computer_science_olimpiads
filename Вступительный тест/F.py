import sys
import json

sp = sys.stdin.read().strip().split('\n')
output_file = open('contact.json', 'w')
data = {"request": {}, "response": {}}
for elem in sp:
    key, value = elem.split(' = ')
    value = int(value)
    if value < 0:
        data["request"][key] = value
    elif value > 0:
        data["response"][key] = value
json.dump(data, output_file)
output_file.close()
