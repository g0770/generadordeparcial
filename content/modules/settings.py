from .mainModules import menuOptions, inputExc, clearCmd
import content.modules.fileManager as fm

def reloadMaxPartes(oldSettings):
  settings = oldSettings
  settings['cantPreguntasMax'] = []
  settings['contenido'] = {}
  for i in range(settings['partes']):
    settings['cantPreguntasMax'].append(fm.obtenerCantidadPreguntasDeTema(i+1))
    settings['contenido'][f'parte {i+1}'] = []
  return settings

def settingsMain(oldSettings, DefaultSettings):
  settings = oldSettings
  while True:
    clearCmd()
    r = menuOptions(typeMsg='settings', responseMsg='Ingrese la opción del menú de opciones a continuación: ')
    match r:
      case 0:
        break
      case 1:
        settings['partes'] = inputExc(int, 'Ingrese la cantidad de partes del parcial a continuación: ')
        settings = reloadMaxPartes(settings)
      case 2:
        settings = DefaultSettings
      case 3:
        settings = reloadMaxPartes(settings)
    input('Enter para continuar... ')
        
  
  return settings
