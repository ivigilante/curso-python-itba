# Une y triunfarás
# Se recibieron distintos postulantes para un empleo de traductor. Crear un diccionario en el cuál la key de cada elemento sea el nombre de un candidato y el contenido sea un set con los idiomas que aprendió. Inventar valores para 5 candidatos.

# Mostrar en pantalla los idiomas que todos los candidatos aprendieron.
# Mostrar en pantalla todos los candidatos que aprendieron por lo menos Español e Inglés.
# El usuario luego debe poder ingresar el nombre de un idioma y el programa deberá mostrar en pantalla el nombre de aquellos candidatos que aprendieron ese idioma.

candidatos = {
	"Pedro": {"Español","Italiano"},
	"Raul": {"Español","Inglés"},
	"Alberto": {"Español","Inglés","Frances","Italiano","Chino"},
	"Luis": {"Español","Frances","Chino"},
	"Ulises": {"Inglés","Italiano"}
}

def mostrar_todos_los_idiomas():
	todos_los_idiomas = set()
	for idiomas in candidatos.values():
		todos_los_idiomas |= idiomas
	print(todos_los_idiomas)
# mostrar_todos_los_idiomas()

def mostrar_esp_ing():
	candidatos_esp_ing = set()
	for candidato, idiomas in candidatos.items():
		if "Español" in idiomas and "Inglés" in idiomas:
			candidatos_esp_ing.add(candidato)
	print(candidatos_esp_ing)
# mostrar_esp_ing()

def buscar_candidato():
	candidatos_buscados = set()
	idioma_buscado = input("Ingrese el idioma a buscar: ")
	for candidato, idiomas in candidatos.items():
		if idioma_buscado in idiomas:
			candidatos_buscados.add(candidato)
	print(candidatos_buscados)
# buscar_candidato()