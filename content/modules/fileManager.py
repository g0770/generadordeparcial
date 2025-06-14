import os

def detectarTemas(onlyTemas:bool = False):
  dir_original = os.getcwd()
  
  os.chdir('./content/enunciados')
  temas = os.listdir()
  if onlyTemas:
    return temas
  temasInfo = []
  for i in temas:
    os.chdir(f'./{i}')
    dictTemp = {
      'nombre': i,
      'partes': os.listdir()
    }
    os.chdir('..')
    temasInfo.append(dictTemp)
  
  os.chdir(dir_original)
  
  return temasInfo

def obtenerCantidadPreguntasDeTema(temaNum:int = 1):
  dir_original = os.getcwd()
  cont = 0
  temasInfo = detectarTemas()
  for tema in temasInfo:
    if f'p{temaNum}.csv' in tema['partes']:
      csv = open(f'./content/enunciados/{tema['nombre']}/p{temaNum}.csv', 'r')
      temp = csv.readlines()
      cont += len(temp)
      csv.close()
      
  os.chdir(dir_original) 
  return cont

def temasQueTieneNParte(temaNum:int = 1):
  dir_original = os.getcwd()
  cont = 0
  temasInfo = detectarTemas()
  temasNombres = []
  for tema in temasInfo:
    if f'p{temaNum}.csv' in tema['partes']:
      temasNombres.append(tema['nombre'])
      
  os.chdir(dir_original) 
  return temasNombres