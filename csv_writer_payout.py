import csv
import json 

with open('sample.json') as js:
    dic_json = json.load(js)

print(type(dic_json))

for x in dic_json['data']:
    print(x)

with open('test_payout.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    count = 0 
    for i in range(len(dic_json['data'])):
        if count == 0:  
            header = dic_json['data'][i].keys()
            writer.writerow(header)
            count += 1
        elif count > 0: 
            writer.writerow(dic_json['data'][i].values())
            count += 1

