import smtplib

receptor = input('Ingrese correo electronico del receptor: ')

#Correo del emisor
emisor = 'ejemplo@gmail.com'

#mensaje del correo
mensaje = 'Hola, este es un mensaje de prueba!'
asunto = 'Prueba de Correo'
mensaje = 'Subject: {}\n\n{}'.format(asunto, mensaje)

#conexion server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()

#autenticar/Colocar correo y contraseña
server.login(user= 'correo@gmail.com', password= 'contraseña')

#emisor, receptor y mensaje/declarado en variables o directo en comillas simples
server.sendmail(emisor, receptor, mensaje)

#salir del servidor
server.quit()

#Mensaje de confirmación
print("Correo enviado")

