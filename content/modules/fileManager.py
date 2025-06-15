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
      try:
        with open(f'./content/enunciados/{tema['nombre']}/p{temaNum}.csv', 'r') as f_in:
          temp = (line.rstrip() for line in f_in) 
          temp = list(line for line in temp if line)
          cont += len(temp)

      except Exception as e:
        print(e)
        input('debug enter para continuar...')
      
  os.chdir(dir_original) 
  return cont

def temasQueTieneNParte(temaNum:int = 1):
  dir_original = os.getcwd()
  temasInfo = detectarTemas()
  temasNombres = []
  for tema in temasInfo:
    if f'p{temaNum}.csv' in tema['partes']:
      temasNombres.append(tema['nombre'])
      
  os.chdir(dir_original) 
  return temasNombres