# Simulacro de Parcial 
## Parte 1
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
### ¿Que imprime este codigo?

	x=5
	print(f'Resultado {x+3}')

 1) Resultado: x+3
 2) Resultado: 53
 3) Resultado: 8
 4) Error

Respuesta correcta: <span style="color: black; background: black;">Resultado: 8</span>
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
### ¿Cual es la salida del siguiente codigo?

	print('Hola', end='*')
	print('Python')

 1) HolaPython
 2) Hola*Python
 3) Hola\nPython
 4) Hola * Python

Respuesta correcta: <span style="color: black; background: black;">Hola*Python
</span>
## Parte 2
### Completa el codigo para mostrar en pantalla todos los archivos en la carpeta actual

	import os
	archivos = os._____(".")
	for a in archivos:
	  print(_____)



Respuesta correcta: <span style="color: black; background: black;">listdir, a</span>
### El siguiente codigo lanza un error. Indica cual y corregilo

	archivo = open("datos.txt", "r")
	lineas = archivo.read()
	print(lineas)
	archivo.closer()



Respuesta correcta: <span style="color: black; background: black;">SyntaxError: archivo.closer() -> archivo.close()
</span>
### Encontra y corregi los errores del siguiente modulo (se guarda como fecha.py)

	import datetime
	def hoy():
	return datetime.today



Respuesta correcta: <span style="color: black; background: black;">  return datetime.now()
</span>
### Completa el codigo para crear un archivo HTML que contenga un titulo "Programacion II" y abra el navegador para mostrarlo

	import webbrowser
	with open("pagina.html","w") as archivo:
	  archivo.write(_____)
	webbrowser.open("_____")



Respuesta correcta: <span style="color: black; background: black;">"Programacion II", pagina.html
</span>
### Completa el codigo para capturar un error si el usuario escribe texto en lugar de un numero

	try:
	  valor = int(input("Ingrese un numero: "))
	  print("Doble:", valor * 2)



Respuesta correcta: <span style="color: black; background: black;">except Exception as e: print("Se ingreso texto")
</span>
