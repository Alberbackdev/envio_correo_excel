import requests
import string
import json
from pandas import json_normalize
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from openpyxl import Workbook
import csv
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

contador=2
#letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
letras = list(string.ascii_uppercase)
#print(letras)

for i in res['vulnerabilities']:
   url = "https://cloud.tenable.com/workbenches/vulnerabilities/"+str(i['plugin_id'])+"/info"
   response2 = requests.request("GET", url, headers=headers)
   res2 = response2.json()
   objeto = res2['info']
   #print(json.dumps(objeto, sort_keys=True, indent=4))
   
   #crea diccionario con letras del abecedario y categorias
   columna = dict(zip(letras,objeto.keys()))
   #crea los titulos de las columnas
   for col, titulo in columna.items():
      sheet[f'{col}1'] = titulo
      pass
      #Agrega info en las celdas correspondientes
      for k, v in objeto.items():
         if titulo == k:
            sheet[f'{col}{contador}'] = '{}'.format(v)

   contador=contador+1  
   print(contador)
book.save('prueba.xlsx')