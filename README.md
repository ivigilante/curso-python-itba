# Curso de Python 2020-2C (ITBA IEEE)
Repositorio dedicado a ejemplos, ejercicios y demás del curso de Python del ITBA IEEE Python2020-2C

## Comandos básicos de Git:
### Clonar repositorio
`git clone https://github.com/ivigilante/curso-python-itba`   
Este comando crea el repositorio git en tu computadora

### Actualizar repositorio local
`git pull`   
Este comando actualiza el repositorio local (en nuestra computadora) con el remoto (el que esta online)

### Subir cambios a repositorio remoto
`git add NOMBRE_DEL_ARCHIVO`  
Este comando agrega el archivo a la lista de cambios que haremos

`git commit -m "MENSAJE PARA NUESTRO CAMBIO"`  
Este comando agrega un mensaje al cambio que haremos para que sea mas entendible que hicimos

`git push`  
Este comando sube los cambios al repositorio remoto
### Cambiar rama de trabajo
`git checkout RAMA`  
Este comando nos permite cambiar a otra rama de trabajo, util cuando queremos trabajar con varias personas a la vez
### Crear una nueva rama de trabajo
`git checkout -b RAMA_NUEVA`  
Este comando crea una rama nueva de trabajo
### Ver ramas de trabajo actuales en el repositorio local
`git branch`   
Este comando muestra las ramas que tenemos en nuestro repositorio local, si queremos una que esta en el remoto, deberemos hacer    
`git checkout RAMA_QUE_QUEREMOS`  
### Ver estado de nuestro repositorio local
`git status`   
Util para ver diferencias y cambios con el repositorio remoto
## Empezar a trabajar!
Primero debemos instalar Git si estamos usando Windows.   
Luego:    
`git clone https://github.com/ivigilante/curso-python-itba`   
`cd curso-python-itba`   
`git checkout primerletradelnombreapellido` (esto es para crear una rama. Si me llamo Raul Pascal, seria rpascal)    
Empezamos a trabajar y una vez que hicimos algo, subimos los cambios:   
`git status` (nos dira que archivos tenemos modificados)   
`git add LosArchivos`   
`git commit -m "MensajeParaElCambio"`   
`git push` 
