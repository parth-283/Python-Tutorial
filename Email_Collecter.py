import json
import re
import requests

url = "https://jsonplaceholder.typicode.com/users"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
r = requests.get(url).text
user_list = json.loads(r)


for i in user_list:
    for key, value in i.items():
        for item in re.findall(regex, str(value)):
            print(i['id'], " : ", item)
