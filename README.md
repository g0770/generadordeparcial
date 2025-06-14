# Generador de Parciales

Programa hecho con Python que genera un simulacro de parcial con varios tipos de preguntas a partir de un conjunto de preguntas posibles
## Formato y como usar
En la carpeta ``./content/enunciados`` se encuentran las carpetas ``pregunta_simple`` y ``salida_codigo`` como ejemplo de los distintos tipos de preguntas que pueden existir en el programa. <br>
Las preguntas se separaran primero por tipo de pregunta, indicado por la carpeta en la que se encuentran, y luego por parte, indicado por el archivo .csv en el que se encuentran.<br>
Cada pregunta seguira el formato: ``pregunta;codigo;respuestas_posibles;respuesta_correcta``
donde los parametros *codigo* y *respuestas_posibles* pueden dejarse vacios para modificar el tipo de pregunta. <br>
Para generar el simulacro solo ejecuta el archivo ``main.py``

## Agregar preguntas
Para agregar preguntas de tipo 'pregunta_simple', solo se necesita crear un .csv llamado 'pN.csv' en la carpeta ``./content/enunciados/pregunta_simple`` donde N representa la parte a la cual pertenecen las preguntas de ese archivo.<br> El csv ademas tiene que seguir el formato indicado en la seccion anterior, teniendo en cuenta a la vez que si hay varias respuestas posibles (tambien aplica para las respuestas correctas), deberan aparecer de esta manera: ``..;respuesta1|respuesta2|..|respuestaN;..``<br>
Si la pregunta incluye un fragmento de codigo de varias lineas, indicar el salto de linea de esta manera: ``..;linea1|linea2|..|lineaN;..``
