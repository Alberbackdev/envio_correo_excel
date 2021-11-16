import requests
import json
f = open('pruebaget.html','w')
url = "https://cloud.tenable.com/workbenches/vulnerabilities"

querystring = {"authenticated":"true","exploitable":"true","resolvable":"true","severity":"high"}

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey=55e23ec9ef4f66275e011f28a0a7d23a3e303a5ff9fb5ae05137a4ae0d68bda4;secretKey=54469980639bd43fe46c48bca7f541c815aaaf78274546260995ec9a44c2e53c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.json()
for i in res['vulnerabilities']:
 url = "https://cloud.tenable.com/workbenches/vulnerabilities/"+str(i['plugin_id'])+"/info"
 response2 = requests.request("GET", url, headers=headers)
 print(response2.text)
