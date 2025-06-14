# Simulacro de Parcial 
## Tema 1
### ¿Que hace el siguiente codigo?

	import webbrowser

	webbrowser.open('https://www.python.org')


 1) Lanza una excepcion
 2) Ejecuta una consola web
 3) Abre el navegador con la url
 4) Nada

Respuesta correcta: <span style="color: black; background: black;">Abre el navegador con la url
</span>
### ¿Que hace deactivate en un entorno virtual?

	


 1) Elimina el entorno
 2) Cierra temporalmente el entorno
 3) Reinicia los paquetes
 4) Actualiza pip

Respuesta correcta: <span style="color: black; background: black;">Cierra temporalmente el entorno
</span>
### ¿Que hace pip freeze > requirements.txt?

	


 1) Muestra los paquetes instalados
 2) Instala paquetes
 3) Elimina pip
 4) Guarda los paquetes instalados en un archivo

Respuesta correcta: <span style="color: black; background: black;">Muestra los paquetes instalados
</span>
### ¿Que hace el siguiente codigo?

	try:

	 x=10/0

	except:

	  print('Error')

	finally:

	  print('Fin')


 1) Solo imprime 'Error'
 2) Solo imprime 'Fin'
 3) Imprime 'Error' y 'Fin'
 4) Lanza una excepcion

Respuesta correcta: <span style="color: black; background: black;">Imprime 'Error' y 'Fin'
</span>
### ¿Cual es la salida del siguiente codigo?

	print('Hola', end='*')

	print('Python')


 1) HolaPython
 2) Hola*Python
 3) Hola\nPython
 4) Hola * Python

Respuesta correcta: <span style="color: black; background: black;">Hola*Python
</span>
### ¿Cual es el uso principal del modulo webbrowser?

	


 1) Crear formularios
 2) Conectarse a bases de datos
 3) Abrir paginas web en el navegador
 4) Descargar imagenes

Respuesta correcta: <span style="color: black; background: black;">Abrir paginas web en el navegador
</span>
### ¿Que hace open('archivo.txt', 'a')?

	


 1) Reemplaza el contenido del archivo
 2) Lee y cierra el archivo
 3) Abre el archivo para agregar contenido
 4) Abre un archivo para lectura binaria

Respuesta correcta: <span style="color: black; background: black;">Abre el archivo para agregar contenido
</span>
### ¿Que hace os.makedirs(""nueva/carpeta"") si no existe?

	


 1) Falla si no existe
 2) Crea solo "carpeta"
 3) Crea todo el arbol de carpetas
 4) Renombra la carpeta actual

Respuesta correcta: <span style="color: black; background: black;">Crea todo el arbol de carpetas</span>
### ¿Que imprime este codigo?

	x=5

	print(f'Resultado {x+3}')


 1) Resultado: x+3
 2) Resultado: 53
 3) Resultado: 8
 4) Error

Respuesta correcta: <span style="color: black; background: black;">Resultado: 8</span>
### ¿Que modulo se usa para trabajar con archivos y rutas?

	


 1) os
 2) random
 3) pip
 4) collections

Respuesta correcta: <span style="color: black; background: black;">os
</span>
### ¿Que hace os.listdir()?

	


 1) Crea un archivo
 2) Lista carpetas disponibles
 3) Lista archivos y carpetas del directorio actual
 4) Cambia de directorio

Respuesta correcta: <span style="color: black; background: black;">Lista carpetas disponibles
</span>
### ¿Cual es el modulo usado para abrir una URL en el navegador desde Python?

	


 1) netbrowser
 2) requests
 3) webbrowser
 4) urllib

Respuesta correcta: <span style="color: black; background: black;">webbrowser
</span>
### ¿Cual de estos errores es capturado con except ZeroDivisionError?

	


 1) Acceso fuera de rango
 2) Division por cero
 3) Conversion de tipo
 4) Archivo no encontrado

Respuesta correcta: <span style="color: black; background: black;">Division por cero
</span>
### ¿Cual es la funcion correcta para obtener la fecha de hoy?

	


 1) os.today()
 2) datetime.now()
 3) datetime.date.today()
 4) date.time.now()

Respuesta correcta: <span style="color: black; background: black;">datetime.now()
</span>
### ¿Que hace pip install -r requirements.txt?

	


 1) Guarda la lista de paquetes
 2) Instala los paquetes listados en el archivo
 3) Elimina todos los paquetes
 4) Crea un entorno virtual

Respuesta correcta: <span style="color: black; background: black;">Instala los paquetes listados en el archivo
</span>
## Tema 2
### Completa el codigo para mostrar en pantalla todos los archivos en la carpeta actual

	import os

	archivos = os._____(".")

	for a in archivos:

	  print(_____)




Respuesta correcta: <span style="color: black; background: black;">listdir, a</span>
### Indica la salida esperada o el error

	lista=[1,2,3]

	print(lista[5])




Respuesta correcta: <span style="color: black; background: black;">IndexError: list index out of range
</span>
### Encontra y corregi los errores del siguiente modulo (se guarda como fecha.py)

	import datetime

	def hoy():

	return datetime.today




Respuesta correcta: <span style="color: black; background: black;">  return datetime.now()
</span>
### El siguiente codigo lanza un error. Indica cual y corregilo

	archivo = open("datos.txt", "r")

	lineas = archivo.read()

	print(lineas)

	archivo.closer()




Respuesta correcta: <span style="color: black; background: black;">SyntaxError: archivo.closer() -> archivo.close()
</span>
### Completa el codigo para capturar un error si el usuario escribe texto en lugar de un numero

	try:

	  valor = int(input("Ingrese un numero: "))

	  print("Doble:", valor * 2)




Respuesta correcta: <span style="color: black; background: black;">except Exception as e: print("Se ingreso texto")
</span>
### Completa el codigo para crear un archivo HTML que contenga un titulo "Programacion II" y abra el navegador para mostrarlo

	import webbrowser

	with open("pagina.html","w") as archivo:

	  archivo.write(_____)

	webbrowser.open("_____")




Respuesta correcta: <span style="color: black; background: black;">"Programacion II", pagina.html
</span>
