import requests
from pandas import json_normalize
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib


#API
url = "https://cloud.tenable.com/workbenches/vulnerabilities"

querystring = {"severity":"critical"}

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey=55e23ec9ef4f66275e011f28a0a7d23a3e303a5ff9fb5ae05137a4ae0d68bda4;secretKey=54469980639bd43fe46c48bca7f541c815aaaf78274546260995ec9a44c2e53c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

#convierte a json y a su vez a csv
data = json_normalize(response.json())

archivo = data.to_excel('report.xlsx', sheet_name='report1')

#----------------------------Correo---------------------

receptor = input('Ingrese correo electronico del receptor: ')

#Correo del emisor
emisor = 'pruebatenable2021@gmail.com'

asunto = 'Reporte de vulnerabilidades'

#Objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = emisor
mensaje['To'] = receptor
mensaje['Subject'] = asunto

adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open('report.xlsx',"rb").read())
adjunto.add_header("content-Disposition",'attachment; filename="report.xlsx"')
mensaje.attach(adjunto)


#conexion server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()

#autenticar/Colocar correo y contraseña
server.login(user= 'pruebatenable2021@gmail.com', password= 'tenable12345')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string().encode('utf-8')

#emisor, receptor y mensaje/declarado en variables o directo en comillas simples
server.sendmail(emisor, receptor, texto)

#salir del servidor
server.quit()

#Mensaje de confirmación
print("Correo enviado")
