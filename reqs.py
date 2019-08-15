import os 
import json 
import requests 
import dotenv 
import socket 


url = "https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json"

res = requests.get(url)
data = json.loads(res.content) 

# data = res.json() 

gov_json = data[0]['legislatures'][0]['popolo_url']
print(gov_json) 


gov_info_url = gov_json 

response = requests.get(gov_info_url)

gov_data = json.loads(response.content) 

person = gov_data['persons'][0]['name']

print(person)


