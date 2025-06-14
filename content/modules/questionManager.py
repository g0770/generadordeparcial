import random

def parseQuestionToStr(pregunta):
  for index, value in enumerate(pregunta):
    try:
      pregunta[index] = value.split('|')
    except:
      pass
  
  pregunta[0] = '### ' + pregunta[0][0]  + '\n'
  pregunta[3] = 'Respuesta correcta: <span style="color: black; background: black;">' + pregunta[3][0] + '</span>'
  
  for i,value in enumerate(pregunta[1]):
    pregunta[1][i] = '\t' + value + '\n'
  if len(pregunta[2]) > 1:
    for i,value in enumerate(pregunta[2]):
      pregunta[2][i] = f' {i+1}) ' + value

  text = ""
  for i,value in enumerate(pregunta):
    if type(value) == type([]):
      texttemp = ""
      for x in value:
        texttemp += x + '\n'
      text += texttemp + '\n'
    else:
      text += value + '\n'
  return text

def questionCreation(data:str = './content/enunciados/', questionType:str = 'salida_codigo', part:str = '1'):

  contenido = open(data+questionType+'/p'+part+'.csv', 'r')
  pregunta = contenido.readlines()
  contenido.close()
  
  pregunta = pregunta[random.randint(0,len(pregunta)-1)]
  pregunta = pregunta.split(';')
  pregunta = parseQuestionToStr(pregunta)

  return pregunta

  
def toMarkDown(preguntas):
  md = open("parciales.md", "w+")
  md.write('# parcial simulado \n')
  
  md.write('## tema 1\n')
  for i in preguntas['tema 1']:
    md.write(i)

  md.write('## tema 2\n')
  for i in preguntas['tema 2']:
    md.write(i)
    
    
  md.close()