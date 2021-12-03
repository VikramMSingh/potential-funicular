import requests
import json
import csv
language=input("Enter programming language ")
url = (f'https://api.github.com/search/repositories?q=language:{language.lower()}' )
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store API response in a variable

response_dict = r.json()

print(response_dict.keys())
data_file = open('%s_file.csv' %language, 'w')

csv_writer = csv.writer(data_file)

count = 0

for keys, values in response_dict:
    if count == 0:
        header = response_dict.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(response_dict.values())
data_file.close()    

#print(response_dict.keys())
#total_repo = response_dict['total_count']
#total_keys = len(response_dict)
#print(f"Keys: {total_keys}")
#for key in sorted(response_dict.keys()):
   # print(key)

#Examining the first repository 

#rep_dict = response_dict['items']
#rep_dict_0 = rep_dict[0]
#rep_dict_key_count = len(rep_dict_0)
#print(f"Keys in a repo: {rep_dict_key_count}")
#for key_repo in rep_dict_0:
#    print(key_repo)
#print(f"Total number of repositories for {language} are: {total_repo}")
##Writing to file
#file_name = "github_data.json"
#open_file = open(file_name,"w")
#json.dump(response_dict, open_file)
#open_file.close()


