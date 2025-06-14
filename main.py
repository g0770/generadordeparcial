import random
import content.modules.questionManager as qm
import content.modules.fileManager as fm
import content.modules.settings as s
from content.modules.mainModules import inputExc, menuOptions, clearCmd

programDefaultSettings = {
  'partes': 2,
  'cantPreguntasMax':  [fm.obtenerCantidadPreguntasDeTema(1), fm.obtenerCantidadPreguntasDeTema(2)],
  'contenido': {
    'parte 1': [],
    'parte 2': []
  }
}
programSettings = programDefaultSettings.copy()

while True:
  clearCmd()
  r = menuOptions(responseMsg='Ingrese la opción del menú principal a continuación: ')
  match r:
    case 0:
      break
    case 1:
      cantP = []
      for index in range(programSettings['partes']):
        while True:
          tempCantPreg = inputExc(int, f"Cuantas preguntas de la Parte {index+1}? (max: {programSettings['cantPreguntasMax'][index]}): ")
          if tempCantPreg >= 0 and tempCantPreg <= programSettings['cantPreguntasMax'][index]:
            break
        cantP.append(tempCantPreg)
      for index, value in enumerate(cantP):
        if value <= 0:
          programSettings['contenido'][f'parte {index+1}'].append('### NO QUESTION FOUND')
        else:
          for i in range(value):
            while True:
              temasPosibles = fm.temasQueTieneNParte(index+1)
              tempQuestion = qm.questionCreation(part=f'{index+1}', questionType=temasPosibles[random.randint(0,len(temasPosibles)-1)])
              if tempQuestion not in programSettings['contenido'][f'parte {index+1}']:
                programSettings['contenido'][f'parte {index+1}'].append(tempQuestion)
                break
    case 2:
      qm.toMarkDown(programSettings['contenido'])
      print("Simulacro generado como 'parciales.md'")
      input('Enter para continuar... ')
    case 3:
      pass
    case 4:
      programSettings = s.settingsMain(programSettings, programDefaultSettings)