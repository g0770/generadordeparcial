
# 🧑‍🎓 Generador de Parciales

Generador de parciales con varios tipos de preguntas a partir de un conjunto de preguntas posibles. Con posibilidad de agregar, borrar o editar las preguntas que quieras ademas de contar con un script facil de utilizar para configurar a tu gusto.

* [💼 Desarrolladores](#desarrolladores)
* [🧩 Tecnologias utilizadas](#tecnologias-utilizadas)
* [🚀 ¿Cómo empezar?](#como-empezar)
  * [▶️ ¿Cómo lo utilizo?](#como-lo-utilizo)
  * [🤔 ¿Cómo añado/edito/borro preguntas?](#como-añado-edito-borro-preguntas)
* [📜 Licencia & Copyright](#licencia-&-copyright)

## 💼 Desarrolladores

Este programa fue desarrollado por Andrés Morales junto a Agustín Maggi. En la pestaña de colaboradores estaran los respectivos enlaces a cada perfil de github.

## 🧩 Tecnologias utilizadas

| Python | defusedxml | FontTools | Fpdf2 | Markdown | pillow |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <img src="https://imgs.search.brave.com/IMLB7FHvpWKelXYxvu7zD7wGW2RkeaYq_CUl3s1YPx4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzcyLzgw/LzJkLzcyODAyZDFl/YjliMGM5ODk5MTRi/ZGE4ZWYxYzZiMGFj/LmpwZw" width=50 height=50> | <img src="" width=50 height=50> | <img src="" width=50 height=50> | <img src="" width=50 height=50> | <img src="" width=50 height=50> | <img src="" width=50 height=50> |



## 🚀 ¿Cómo empezar?

1) Clonar el repositorio

    git clone https://github.com/g0770/generadordeparcial.git

2) Navegar a la carpeta creada

    cd generadordeparcial

3) Instalar las dependencias

    pip install -r requirements.txt

### ▶️ ¿Cómo lo utilizo?

<iframe width="560" height="315" src="https://www.youtube.com/embed/Inbg9Pcu7u8?si=vMlHPHc7OZvnpmH3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Estando dentro de la carpeta 'generadordeparcial' deberia encontrarse un archivo llamado main.py. Se deberá de ejecutar este mismo para empezar el programa.

A continuación se mostrara un pequeño menú en una consola, debera de escribirse en ella el numero de opcion correspondiente para poder utilizarlo.

Siempre que se abra de nuevo el programa, todo funcionamiento del programa volvera a su estado predeterminado, por ende si es necesario cambiar la configuración hay que recordar que una vez cerremos el programa se perderá. No hay planes para arreglar esta cuestion.

### 🤔 ¿Cómo añado/edito/borro preguntas?

Antes de crear una pregunta nueva debemos de conocer que son los TEMAS y las PARTES.

Cada pregunta tendra un solo tema, este será definido por las carpetas que se creen dentro de /content/enunciados. Un tema es un titulo que describe brevemente que tipo de pregunta es.

Ademas dentro de la carpeta de cada tema, se debera dividir las preguntas por parte con este formato: <b>pN.csv</b>

* p: Parte
* N: Numero de parte
* .csv: el formato de archivo en donde se guardaran las preguntas

<br>
El parcial generado podrá divirse por partes, por defecto tendremos 2, es decir parte 1 y parte 2. La division por partes funciona como un indicador de dificultad, es decir, mientras mayor sea el numero mas dificil va a ser. Se tiene contemplada la posibilidad de tener infinitas partes, sin embargo recomendamos solamente hacer uso de 3.

Una vez entendido los temas y las partes, tomemos de ejemplo /content/enunciados/salida_codigo. Este tema simplemente se refiere a preguntas en donde hay que decifrar la salida de un codigo escrito en python.

Si quisiesemos agregar una pregunta, debemos dirigirnos a dicha carpeta y, por ejemplo, seleccionar la parte 1 (p1.csv) para agregar una pregunta de dificultad 1.

Una vez dentro agregamos una nueva linea, o editamos una existente, con este formato:

    PREGUNTA ; CODIGO ; MULTIPLECHOICE ; RESPUESTACORRECTA

<i>En el caso de que se quiera utilizar alguno de los campos, simplemente se deja vacio, importante que la cantidad de ; sea siempre la misma porque de lo contrario desembocaria en varios errores que no tengo ganas de contemplar en el codigo.</i>

* PREGUNTA: se refiere a la pregunta que el alumno deberá responder.
* CODIGO: un codigo que podra verse por el usuario, se puede utilizar como descripcion si se desea.
* MULTIPLE CHOICE: las posibles opciones que puede llegar a tener una pregunta, si no se quiere se puede dejar vacio o utilizar como otro campo.
* RESPUESTA CORRECTA: la respuesta correcta del problema/pregunta.

Cada campo podra tener un salto de linea y propia tabulacion, y este debe ser escrito con el cáracter "|", y si uno lo desea, una tabulacion luego de este caracter. Por ejemplo:

<b><i>Describir que está mal con este código:

    x='hello world'
      print(X)

  - Se referencia mal la variable 'x'
  - Está mal escrito print

Respuesta correcta: Se referencia mal la variable 'x'</i></b>

Para poder agregar esta pregunta deberemos escribirla en una nueva linea en p1.csv:

    Describir que está mal con este código:;x='hello world'|  print(X);Se referencia mal la variable 'x'|Está mal escrito print;Se referencia mal la variable 'x'

* PREGUNTA: Describir que está mal con este código:;
* CODIGO: x='hello world'|  print(X);
* MULTIPLE CHOICE: Se referencia mal la variable 'x'|Está mal escrito print;
* RESPUESTA CORRECTA: Se referencia mal la variable 'x'

<i>Si el archivo de la parte (por ejemplo parte3 seria p3.csv) no existe, puede crearse a mano y el programa lo detectara siempre y cuando se respete la estructura de las carpetas dentro de enunciados.</i>

---
Cuando querramos borrar una pregunta, deberemos de borrar la linea entera. <b>IMPORTANTE borrar toda la linea entera, no puede quedar ni un espacio en blanco.</b>

## 📜 Licencia & Copyright
Ninguna, suerte entendiendo el código.