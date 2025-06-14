
import os

def inputExc(tipo = str, msg:str = 'Ingrese el dato a continuación: '):
  while True:
    try:
      resp = tipo(input(msg))
      break
    except Exception as e:
      print(e)
  return resp

def clearCmd():
  try:
    os.system('cls') 
  except:
    os.system('clear')

def menuOptions (typeMsg:str = 'main', needsResponse:bool = True, responseMsg:str = 'Ingrese el dato a continuación: '):
  match typeMsg:
    case 'main':
      print('[1] GENERAR NUEVAS PREGUNTAS')
      print('[2] IMPORTAR A .MD')
      print('[3] IMPORTAR A .PDF')
      print('[4] OPCIONES DE PROGRAMA')
      print('[0] SALIR DEL PROGRAMA')
    case 'settings':
      print('[1] CAMBIAR CANTIDAD DE PARTES')
      print('[2] DEVOLVER LOS VALORES A SU VALOR DEFAULT')
      print('[3] RECARGAR CANTIDAD MAXIMA DE PREGUNTAS (DE PARTE)')
      print('[0] VOLVER')
      
  
  if needsResponse:
    response = inputExc(int,msg=responseMsg)
    return response


