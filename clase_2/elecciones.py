# Las elecciones
# Realizar un programa en el cual se decida cual es el ganador de una elección a presidente

# En el diccionario candidatos la clave es el nombre del cadidato y el contenido la cantidad de votos.

# Hint: Usen for, if, variables auxiliares.
candidatos = {
    "Michael Jackson": 34453,
    "Oliver Kahn": 18445,
    "Walt Disney": 5434444,
    "John Lennon": 12332,
    "Roque Sáenz Peña": 5543,
    "Alexandria Ocasio-Cortez": 343343,
    "Ludwig van Beethoven":1232322
}

# for nombre, votos in candidatos.items():
#     print(nombre,":", votos)

def encontrarGanador(candidatos):
	return max(candidatos, key = candidatos.get)

def esBallotage(candidatos, ganador):
	votos_totales = sum(candidatos.values())
	if candidatos[ganador] < (votos_totales/2) + 1 :
		return True
	return False

ganador = encontrarGanador(candidatos)
ballotage = esBallotage(candidatos,ganador)

if ballotage:
	print("{} gano las votaciones pero habra ballotage ya que saco {} votos".format(ganador, candidatos[ganador]))
else:
	print("{} es el ganador de las elecciones con {} votos!".format(ganador, candidatos[ganador]))

# Hacer que el programa anterior indique si debe haber ballotage (es decir, si el ganador obtuvo menos del 50%+1 de los votos).
