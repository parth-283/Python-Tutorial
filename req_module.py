import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(r.text, "\n\n\n")

payload = {
    'name': 'Parth Kathiriya',
    'degree': 'MCA'
}

res = requests.post('https://httpbin.org/post', data=payload)
print(res.text)
