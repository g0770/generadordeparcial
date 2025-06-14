
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
      print('[1] GENERATE NEW QUESTIONS')
      print('[2] IMPORT TO .MD AND .PDF')
      print('[3] PROGRAM SETTINGS')
      print('[0] EXIT PROGRAM')
    case 'settings':
      print('[1] CHANGE AMOUNT OF "TIPOS"')
      print('[2] SET TO DEFAULT SETTINGS')
      print('[3] RELOAD AMOUNT OF QUESTIONS (FOR EVERY STEP)')
      print('[0] GO BACK')
      
  
  if needsResponse:
    response = inputExc(int,msg=responseMsg)
    return response


