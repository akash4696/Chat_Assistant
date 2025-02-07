import requests

url = "http://127.0.0.1:5001/query"
payload = {"query": "what is the total salary expense for the Sales department."}

response = requests.post(url, json=payload)
print(response.json())
