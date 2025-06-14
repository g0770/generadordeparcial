import random
import content.modules.questionManager as qm
import content.modules.fileManager as fm

#TODO PASAR LAS PREGUNTAS
#TODO CREAR PARTE 3
#TODO CHUPAR PIJA ok hecho DONE

def inputExc(tipo = str, msg = 'Ingrese el dato a continuación: '):
  while True:
    try:
      resp = tipo(input(msg))
      break
    except Exception as e:
      print(e)
  return resp

cantTotalPreguntasParte1 = fm.obtenerCantidadPreguntasDeTema(1)
cantTotalPreguntasParte2 = fm.obtenerCantidadPreguntasDeTema(2)

cantParte1, cantParte2 = 0, 0
while True:
  cantParte1 = inputExc(int, f"Cuantas preguntas de la Parte 1? (max: {cantTotalPreguntasParte1}): ")
  if cantParte1 >= 0 and cantParte1 <= cantTotalPreguntasParte1:
    break
while True:
  cantParte2 = inputExc(int, f"Cuantas preguntas de la Parte 2? (max: {cantTotalPreguntasParte2}): ")
  if cantParte2 >= 0 and cantParte2 <= cantTotalPreguntasParte2:
    break

parte1Preguntas = []
parte2Preguntas = []

for i in range(cantParte1):
  while True:
    temasPosibles = fm.temasQueTieneNParte(1)
    tempQuestion = qm.questionCreation(part='1', questionType=temasPosibles[random.randint(0,len(temasPosibles)-1)])
    if tempQuestion not in parte1Preguntas:
      parte1Preguntas.append(tempQuestion)
      break
  
for i in range(cantParte2):
  while True:
    temasPosibles = fm.temasQueTieneNParte(2)
    tempQuestion = qm.questionCreation(part='2', questionType=temasPosibles[random.randint(0,len(temasPosibles)-1)])
    if tempQuestion not in parte2Preguntas:
      parte2Preguntas.append(tempQuestion)
      break

contenido = {
  'tema 1': parte1Preguntas,
  'tema 2': parte2Preguntas
}

qm.toMarkDown(contenido)
print("Simulacro generado como 'parciales.md'")