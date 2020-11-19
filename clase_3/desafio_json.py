# Estás encargado de un servidor con millones de usuarios.

# Se te pide escribir un programa que lea el email y contraseña del usuario y se fije si existe el usuario y si coincide la contraseña.

# Se tienen datos encolumnados en formato JSON que nos llegan del siguiente formato:

# {
#     "usuarios": ["mica@mail.co", "jerry@gma.com","alber@soup.co"],
#     "contra": ["abc123","caballitos","yoloswag"]
# }
# La entrada del programa son tres lineas! El programa entonces va tener tres input()s. La primer linea contiene el JSON, la segunda el email a verificar, y la tercera la contraseña. Por ende, las primeras lineas de su programa seguro sean:

# import json
# usuarios = json.loads(input())
# email = input()
# password = input()
# La salida del programa tiene que imprimir OK si el usuario se encuentra en la base de datos y si coincide la contraseña, imprimimos DNE (does not exist) si el usuario no existe y NO en cualquier otro caso.

import json
db = json.loads(input())
email = input()
password = input()

if email not in db["usuarios"]:
	print("DNE")
else:
	if password != db["contra"][db["usuarios"].index(email)]:
		print("NO")
	else:
		print("OK")