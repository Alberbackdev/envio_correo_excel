import requests
import json
from pandas import json_normalize
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from openpyxl import Workbook
import smtplib


#API
url = "https://cloud.tenable.com/workbenches/vulnerabilities"

querystring = {"authenticated":"true","exploitable":"true","resolvable":"true","severity":"high"}

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey=55e23ec9ef4f66275e011f28a0a7d23a3e303a5ff9fb5ae05137a4ae0d68bda4;secretKey=54469980639bd43fe46c48bca7f541c815aaaf78274546260995ec9a44c2e53c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.json()
book = Workbook()
sheet = book.active
sheet ['A1'] = 'description'
sheet ['B1'] = 'synopsis'
sheet ['C1'] = 'solution'
columnas= ['A', 'B', 'C']
contador=2
for i in res['vulnerabilities']:
 url = "https://cloud.tenable.com/workbenches/vulnerabilities/"+str(i['plugin_id'])+"/info"
 response2 = requests.request("GET", url, headers=headers)
 res2 = response2.json()
 objeto = res2['info']
 titulo = objeto.keys()
 valores = objeto.values()
 elementos = objeto.items()
 for titulo, valores in elementos:
    #print(titulo, '-->', valores)
    if titulo=='description' or titulo=='synopsis' or titulo=='solution':
        for i2 in columnas:
         #print(titulo, '-->', valores)
            sheet[f'{i2}{contador}'] = valores
        contador=contador+1  
        print(contador)
 #print(json.dumps(objeto, sort_keys=True, indent=4))
book.save('prueba.xlsx')