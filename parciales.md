# Simulacro de Parcial 

## Parte 1
### ¿Que hace deactivate en un entorno virtual?

	

 1) Elimina el entorno
 2) Cierra temporalmente el entorno
 3) Reinicia los paquetes
 4) Actualiza pip

Respuesta correcta: <p style="color: black; background: black;">Cierra temporalmente el entorno</p>
### ¿Cual de estos errores es capturado con except ZeroDivisionError?

	

 1) Acceso fuera de rango
 2) Division por cero
 3) Conversion de tipo
 4) Archivo no encontrado

Respuesta correcta: <p style="color: black; background: black;">Division por cero</p>
### ¿Qué hace datetime.datetime.now() en Python? 

	 import datetime
	print(datetime.datetime.now()) 

 1)  Devuelve la fecha y hora actual
 2) Cierra el programa
 3) Borra el caché
 4) Compara dos fechas 

Respuesta correcta: <p style="color: black; background: black;"> Devuelve la fecha y hora actual
</p>
### ¿Que hace el siguiente codigo?

	import webbrowser
	webbrowser.open('https://www.python.org')

 1) Lanza una excepcion
 2) Ejecuta una consola web
 3) Abre el navegador con la url
 4) Nada

Respuesta correcta: <p style="color: black; background: black;">Abre el navegador con la url
</p>
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

## Parte 2
### Agregar return

	def division(a, b)

 

Respuesta correcta: <p style="color: black; background: black;"> def division(a, b):</p>
### Encontra y corregi los errores del siguiente modulo (se guarda como fecha.py)

	import datetime
	def hoy():
	return datetime.today



Respuesta correcta: <p style="color: black; background: black;">  return datetime.now()
</p>
### El siguiente codigo lanza un error. Indica cual y corregilo

	archivo = open("datos.txt", "r")
	lineas = archivo.read()
	print(lineas)
	archivo.closer()



Respuesta correcta: <p style="color: black; background: black;">SyntaxError: archivo.closer() -> archivo.close()
</p>
### Transforma esta declaración en una con valor por defecto

	 def imprimir(texto)

 

Respuesta correcta: <p style="color: black; background: black;"> def imprimir(texto='Hello'):
</p>

## Parte 3
### Crea una función `maximo` que acepte una lista de enteros y retorne el más grande. 

	 

 

Respuesta correcta: <p style="color: black; background: black;"> def maximo(numeros: list[int]) -> int:\n    return max(numeros)
</p>
### Simulá la creación de un entorno virtual y la instalacion del paquete cowsay. Incluí creacion, activación, instalación y exportación de requerimientos

	



Respuesta correcta: <p style="color: black; background: black;">python3 -m venv entorno</p>
### Crea una función que abra una lista de URLs una tras otra en nuevas pestañas.

	 

 

Respuesta correcta: <p style="color: black; background: black;"> def abrir_varias(urls: list[str]):</p>
### Dado el siguiente codigo, explica el resultado e indica si hay error

	def agregar(lista=[]):
		lista.append('x')
		return lista
	print(agregar())
	print(agregar())



Respuesta correcta: <p style="color: black; background: black;">imprime ['x'] y despues ['x','x'], no tira ningun error</p>
### Crea una función `unir` que reciba varias cadenas y las concatene con espacios. 

	 

 

Respuesta correcta: <p style="color: black; background: black;"> def unir(*cadenas: str) -> str:\n    return " ".join(cadenas)
</p>
