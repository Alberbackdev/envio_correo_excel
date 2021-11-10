import requests

url = "https://cloud.tenable.com/workbenches/vulnerabilities"

querystring = {"severity":"critical"}

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey=55e23ec9ef4f66275e011f28a0a7d23a3e303a5ff9fb5ae05137a4ae0d68bda4;secretKey=54469980639bd43fe46c48bca7f541c815aaaf78274546260995ec9a44c2e53c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)