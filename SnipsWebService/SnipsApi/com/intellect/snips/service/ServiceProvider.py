import http.client
import json



conn = http.client.HTTPSConnection('http://192.168.43.64:8000')

headers = {'Content-type': 'application/json'}

data = {
    "text": "bit details for apple"
}
json_data = json.dumps(data)

conn.request('POST', '/parseNLUText', json_data, headers)

response = conn.getresponse()
print(response.read().decode())