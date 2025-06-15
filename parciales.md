# Simulacro de Parcial 

## Parte 1
### ¿Que hace pip install -r requirements.txt?

	

 1) Guarda la lista de paquetes
 2) Instala los paquetes listados en el archivo
 3) Elimina todos los paquetes
 4) Crea un entorno virtual

Respuesta correcta: <p style="color: black; background: black;">Instala los paquetes listados en el archivo
</p>
### ¿Cual de estos errores es capturado con except ZeroDivisionError?

	

 1) Acceso fuera de rango
 2) Division por cero
 3) Conversion de tipo
 4) Archivo no encontrado

Respuesta correcta: <p style="color: black; background: black;">Division por cero</p>
### ¿Que hace pip freeze > requirements.txt?

	

 1) Muestra los paquetes instalados
 2) Instala paquetes
 3) Elimina pip
 4) Guarda los paquetes instalados en un archivo

Respuesta correcta: <p style="color: black; background: black;">Muestra los paquetes instalados</p>
### ¿Cual es la funcion correcta para obtener la fecha de hoy?

	

 1) os.today()
 2) datetime.now()
 3) datetime.date.today()
 4) date.time.now()

Respuesta correcta: <p style="color: black; background: black;">datetime.now()</p>
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
### Encontra y corregi los errores del siguiente modulo (se guarda como fecha.py)

	import datetime
	def hoy():
	return datetime.today



Respuesta correcta: <p style="color: black; background: black;">  return datetime.now()</p>
### El siguiente codigo lanza un error. Indica cual y corregilo

	archivo = open("datos.txt", "r")
	lineas = archivo.read()
	print(lineas)
	archivo.closer()



Respuesta correcta: <p style="color: black; background: black;">SyntaxError: archivo.closer() -> archivo.close()
</p>
### Completa el codigo para mostrar en pantalla todos los archivos en la carpeta actual

	import os
	archivos = os._____(".")
	for a in archivos:
	  print(_____)



Respuesta correcta: <p style="color: black; background: black;">listdir, a</p>
### Completa el codigo para capturar un error si el usuario escribe texto en lugar de un numero

	try:
	  valor = int(input("Ingrese un numero: "))
	  print("Doble:", valor * 2)



Respuesta correcta: <p style="color: black; background: black;">except Exception as e: print("Se ingreso texto")
</p>
### Completa el codigo para crear un archivo HTML que contenga un titulo "Programacion II" y abra el navegador para mostrarlo

	import webbrowser
	with open("pagina.html","w") as archivo:
	  archivo.write(_____)
	webbrowser.open("_____")



Respuesta correcta: <p style="color: black; background: black;">"Programacion II", pagina.html
</p>

## Parte 3
### Simulá la creación de un entorno virtual y la instalacion del paquete cowsay. Incluí creacion, activación, instalación y exportación de requerimientos

	



Respuesta correcta: <p style="color: black; background: black;">python3 -m venv entorno</p>
### Dado el siguiente codigo, explica el resultado e indica si hay error

	def agregar(lista=[]):
		lista.append('x')
		return lista
	print(agregar())
	print(agregar())



Respuesta correcta: <p style="color: black; background: black;">imprime ['x'] y despues ['x','x'], no tira ningun error</p>
### Usando *args, escribí una funcion que devuela el mayor de todos los valores ingresados

	



Respuesta correcta: <p style="color: black; background: black;">def max_args(*args):</p>
### Implementá una función que reciba un string y retorne la longitud de la última palabra

	



Respuesta correcta: <p style="color: black; background: black;">def longitud_ultima_palabra(texto):</p>
### Escribí una funcion que reciba un numero de DNI y retorne true si tiene 7 u 8 digitos validos, false si no

	



Respuesta correcta: <p style="color: black; background: black;">def verificar_dni(dni):</p>
