from fpdf import FPDF
import markdown
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
    pregunta[1][i] = '\t' + value
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

  
def toMarkDown(contenido):
  md = open("parciales.md", "w+")
  md.write('# Simulacro de Parcial \n')
  
  for index,value in contenido['contenido'].items():
    md.write(f'## {index.title()}\n')
    for i in value:
      md.write(i)  
    
  md.close()

def markdownToPDF(md):
  try:
    archivo = open(md, "r")
    text = archivo.read()
    archivo.close()
    html = markdown.markdown(text)
    
    pdf = FPDF()
    pdf.add_page()

    pdf.write_html(html)
    pdf.output("parciales.pdf")
  except Exception as e:
    print(e)

markdownToPDF("parciales.md")