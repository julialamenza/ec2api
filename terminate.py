import requests
import json

url = 'http://localhost:8080/api/terminate'

data = {
    "region_name": "us-east-1",
    "instance_id": "i-08d0e5a2b5468b9cb"
}

data = json.dumps(data)

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=data, headers=headers)

print(response.text)
