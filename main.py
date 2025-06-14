import random
import content.modules.questionManager as qm
import content.modules.fileManager as fm
from content.modules.mainModules import inputExc,menuOptions

programDefaultSettings = {
  'temas': 3,
  'cantPreguntasMax':  [fm.obtenerCantidadPreguntasDeTema(1), fm.obtenerCantidadPreguntasDeTema(2), fm.obtenerCantidadPreguntasDeTema(3)]
}
programSettings = programDefaultSettings.copy()

contenido = {
  'tema 1': [],
  'tema 2': []
}

while True:
  r = menuOptions()
  match r:
    case 1:
      cantP = []
      for index in range(programSettings['temas']):
        while True:
          tempCantPreg = inputExc(int, f"Cuantas preguntas de la Parte {index+1}? (max: {programSettings['cantPreguntasMax'][index]}): ")
          if cantParte1 >= 0 and cantParte1 <= programSettings['cantPreguntasMax'][index]:
            break
        cantP.append(tempCantPreg)

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



qm.toMarkDown(contenido)
print("Simulacro generado como 'parciales.md'")