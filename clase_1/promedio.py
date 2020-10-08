# Cálculo de promedio
# Cálcular la nota de un alumno es una tarea cotidiana de un profesor. 
# Esta tarea suele realizarse a mano o en excel muchas veces. 
# En esta ocasión la haremos en python.
# Escribir una función que calcule el promedio de 3 notas y entrege 
# ese valor usando return.
# Reescribir la función anterior modificandola 
# para asignar una importancia al primer examen de 20%, 
# al segundo de 50% y al tercero de 30%.
# Llamar a cada función anterior 3 veces con 
# distintas notas y verificar, mediante la instrucción if, si el alumno 
# aprobó en cada caso (suponga que 4 es la nota de aprobación).
def promedio(n1, n2, n3):
	return (n1 + n2 + n3) / 3

def promedioImportancia(n1, n2, n3):
	return (n1 * 0.2 + n2 * 0.5 + n3 * 0.3)

def evaluarAlumno(nombre, n1, n2, n3, func_promedio):
	prom = func_promedio(n1,n2,n3)
	if prom >= 4:
		print(nombre + " aprobo")
	else:
		print(nombre + " desaprobo")