import json

numbers = [2,3,4,5,6,7,8]

filename = "numbers.json"

open_file = open(filename,"w")
json.dump(numbers,open_file)

open_file.close()
