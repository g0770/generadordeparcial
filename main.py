import random
import content.modules.questionManager as qm
import content.modules.fileManager as fm
import content.modules.settings as s
from content.modules.mainModules import inputExc, menuOptions, clearCmd

#variables del programa

programDefaultSettings = {
  'partes': 3,
  'cantPreguntasMax':  [fm.obtenerCantidadPreguntasDeTema(1), fm.obtenerCantidadPreguntasDeTema(2), fm.obtenerCantidadPreguntasDeTema(3)],
  'contenido': {
    'parte 1': [],
    'parte 2': [],
    'parte 3': []
  }
}
programSettings = programDefaultSettings.copy()

#funciones

def generateQuestions():
  global programSettings
  
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

#main

generateQuestions()
while True:
  try:
    clearCmd()
    r = menuOptions(responseMsg='Ingrese la opción del menú principal a continuación: ')
    match r:
      case 0:
        break
      case 1:
        generateQuestions()
      case 2:
        qm.toMarkDown(programSettings)
        print("Simulacro generado como 'parciales.md'")
        input('Enter para continuar... ')
      case 3:
        qm.toPDF(programSettings)
        print("Simulacro generado como 'parciales.pdf'")
        input('Enter para continuar... ')
      case 4:
        programSettings = s.settingsMain(programSettings, programDefaultSettings)
  except Exception as e:
    print(e)
    input('debug enter para continuar... ')