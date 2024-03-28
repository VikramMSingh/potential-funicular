import json

filename = 'numbers.json'

open_file = open(filename,"r")
numbers = json.load(open_file)

print(numbers)
