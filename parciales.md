# Simulacro de Parcial 
## Parte 1
### ¿Cual es el uso principal del modulo webbrowser?

	

 1) Crear formularios
 2) Conectarse a bases de datos
 3) Abrir paginas web en el navegador
 4) Descargar imagenes

Respuesta correcta: <p style="color: black; background: black;">Abrir paginas web en el navegador
</p>
### ¿Que imprime este codigo?

	x=5
	print(f'Resultado {x+3}')

 1) Resultado: x+3
 2) Resultado: 53
 3) Resultado: 8
 4) Error

Respuesta correcta: <p style="color: black; background: black;">Resultado: 8</p>
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

Respuesta correcta: <p style="color: black; background: black;">Imprime 'Error' y 'Fin'
</p>
### ¿Que hace open('archivo.txt', 'a')?

	

 1) Reemplaza el contenido del archivo
 2) Lee y cierra el archivo
 3) Abre el archivo para agregar contenido
 4) Abre un archivo para lectura binaria

Respuesta correcta: <p style="color: black; background: black;">Abre el archivo para agregar contenido
</p>
### ¿Que modulo se usa para trabajar con archivos y rutas?

	

 1) os
 2) random
 3) pip
 4) collections

Respuesta correcta: <p style="color: black; background: black;">os
</p>
## Parte 2
### Completa el codigo para crear un archivo HTML que contenga un titulo "Programacion II" y abra el navegador para mostrarlo

	import webbrowser
	with open("pagina.html","w") as archivo:
	  archivo.write(_____)
	webbrowser.open("_____")



Respuesta correcta: <p style="color: black; background: black;">"Programacion II", pagina.html
</p>
### Completa el codigo para mostrar en pantalla todos los archivos en la carpeta actual

	import os
	archivos = os._____(".")
	for a in archivos:
	  print(_____)



Respuesta correcta: <p style="color: black; background: black;">listdir, a</p>
### El siguiente codigo lanza un error. Indica cual y corregilo

	archivo = open("datos.txt", "r")
	lineas = archivo.read()
	print(lineas)
	archivo.closer()



Respuesta correcta: <p style="color: black; background: black;">SyntaxError: archivo.closer() -> archivo.close()
</p>
### Encontra y corregi los errores del siguiente modulo (se guarda como fecha.py)

	import datetime
	def hoy():
	return datetime.today



Respuesta correcta: <p style="color: black; background: black;">  return datetime.now()
</p>
### Indica la salida esperada o el error

	lista=[1,2,3]
	print(lista[5])



Respuesta correcta: <p style="color: black; background: black;">IndexError: list index out of range
</p>
