import random
import content.modules.questionManager as qm
import content.modules.fileManager as fm
from content.modules.mainModules import inputExc, menuOptions, clearCmd

programDefaultSettings = {
  'temas': 2,
  'cantPreguntasMax':  [fm.obtenerCantidadPreguntasDeTema(1), fm.obtenerCantidadPreguntasDeTema(2), fm.obtenerCantidadPreguntasDeTema(3)]
}
programSettings = programDefaultSettings.copy()

contenido = {
  'tema 1': [],
  'tema 2': []
}

while True:
  clearCmd()
  r = menuOptions()
  match r:
    case 0:
      break
    case 1:
      cantP = []
      for index in range(programSettings['temas']):
        while True:
          tempCantPreg = inputExc(int, f"Cuantas preguntas de la Parte {index+1}? (max: {programSettings['cantPreguntasMax'][index]}): ")
          if tempCantPreg >= 0 and tempCantPreg <= programSettings['cantPreguntasMax'][index]:
            break
        cantP.append(tempCantPreg)
      for index, value in enumerate(cantP):
        for i in range(value):
          while True:
            temasPosibles = fm.temasQueTieneNParte(index+1)
            tempQuestion = qm.questionCreation(part=f'{index+1}', questionType=temasPosibles[random.randint(0,len(temasPosibles)-1)])
            if tempQuestion not in contenido[f'tema {index+1}']:
              contenido[f'tema {index+1}'].append(tempQuestion)
              break
    case 2:
      qm.toMarkDown(contenido)
      print("Simulacro generado como 'parciales.md'")
      input('Enter para continuar... ')