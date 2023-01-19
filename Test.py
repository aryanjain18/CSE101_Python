city_name = 'Delhi'

import requests

#1. City Data - latitude, longitude, country, population
api_url = 'https://api.api-ninjas.com/v1/city?name='+city_name
response = requests.get(api_url, headers={'X-Api-Key': 'Cc2e3MXMCL67SzyeEwVjZA==Tj72dKhqQmr35cyg'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)