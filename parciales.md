# Simulacro de Parcial 
## Parte 1
### ¿Que hace pip freeze > requirements.txt?

	

 1) Muestra los paquetes instalados
 2) Instala paquetes
 3) Elimina pip
 4) Guarda los paquetes instalados en un archivo

Respuesta correcta: <span style="color: black; background: black;">Muestra los paquetes instalados
</span>
### ¿Que hace pip install -r requirements.txt?

	

 1) Guarda la lista de paquetes
 2) Instala los paquetes listados en el archivo
 3) Elimina todos los paquetes
 4) Crea un entorno virtual

Respuesta correcta: <span style="color: black; background: black;">Instala los paquetes listados en el archivo
</span>
### ¿Cual de estos errores es capturado con except ZeroDivisionError?

	

 1) Acceso fuera de rango
 2) Division por cero
 3) Conversion de tipo
 4) Archivo no encontrado

Respuesta correcta: <span style="color: black; background: black;">Division por cero
</span>
### ¿Que imprime este codigo?

	x=5
	print(f'Resultado {x+3}')

 1) Resultado: x+3
 2) Resultado: 53
 3) Resultado: 8
 4) Error

Respuesta correcta: <span style="color: black; background: black;">Resultado: 8</span>
### ¿Cual es el uso principal del modulo webbrowser?

	

 1) Crear formularios
 2) Conectarse a bases de datos
 3) Abrir paginas web en el navegador
 4) Descargar imagenes

Respuesta correcta: <span style="color: black; background: black;">Abrir paginas web en el navegador
</span>
## Parte 2
### Indica la salida esperada o el error

	lista=[1,2,3]
	print(lista[5])



Respuesta correcta: <span style="color: black; background: black;">IndexError: list index out of range
</span>
### Completa el codigo para mostrar en pantalla todos los archivos en la carpeta actual

	import os
	archivos = os._____(".")
	for a in archivos:
	  print(_____)



Respuesta correcta: <span style="color: black; background: black;">listdir, a</span>
### Completa el codigo para crear un archivo HTML que contenga un titulo "Programacion II" y abra el navegador para mostrarlo

	import webbrowser
	with open("pagina.html","w") as archivo:
	  archivo.write(_____)
	webbrowser.open("_____")



Respuesta correcta: <span style="color: black; background: black;">"Programacion II", pagina.html
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
