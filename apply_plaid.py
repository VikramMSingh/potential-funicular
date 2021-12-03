import json
import requests

#with open('plaid.json', 'r') as json_file:
#    r = json.load(json_file)

url = "https://contact.plaid.com/jobs"
data = {
  "name": "Vikram Singh",
  "email": "vikram.m.singh@case.edu",
  "resume": "https://drive.google.com/file/d/1Os-EM2msuLVDL0zi-00Jzek23jsegZdN/view?usp=sharing",
  "phone": "216-820-7251",
  "job_id": "44315360-73bb-4c5d-990d-67fe3f1eba34",
  "github": "https://github.com/VikramMSingh",
  "website": "www.propomate.com",
  "location": "Cleveland, OH",
  "favorite_candy": "Hersheys Almond kisses",
  "superpower": "Problem basher"
}

data = json.dumps(data)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} 
response = requests.post(url, data, headers)

print(response.status_code, response.reason, response.text)
