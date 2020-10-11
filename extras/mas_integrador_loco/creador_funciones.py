contador = 0
file = open("funciones_matematicas.py","w")
funcs = {}
def print_contador():
	print(contador)
def aumentar_contador():
	global contador
	contador += 1

def crear_funcion():
	ecuacion = input("Ingrese ecuacion: ")
 
def agregar_funcion():
	f = open("funciones_matematicas.py","w")
	ecuacion = input("Ingrese ecuacion: ")
	f.write("funcs = \{}\n")
	f.write("def f1(x):\n")
	f.write("\treturn "+ecuacion)
	f.close()
def test_func():
	f = open("funciones_matematicas.py","w")
	f.write("def f():\n")
	f.write("\tprint(\"hola\")")
	f.close()