from fpdf import FPDF, TextStyle, HTMLMixin
import mistletoe
import random

def parseQuestionToStr(pregunta):
  for index, value in enumerate(pregunta):
    try:
      pregunta[index] = value.split('|')
    except:
      pass
  
  pregunta[0] = '### ' + pregunta[0][0]  + '\n'
  pregunta[3] = 'Respuesta correcta: <p style="color: black; background: black;">' + pregunta[3][0] + '</p>'
  
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
    md.write(f'\n## {index.title()}\n')
    for i in value:
      md.write(i)  
    
  md.close()

def toPDF(contenido):
  pdf = FPDF()
  pdf.set_font("Times", style="B", size=24)
  pdf.add_page()
  pdf.multi_cell(w=0, text="Simulacro de parcial\n", align="c")
  pdf.set_font("Helvetica", size=16)
  for index,value in contenido['contenido'].items():
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=18)
    pdf.multi_cell(w=0, text=f"{index.title()}\n")
    for i in value:
      pdf.set_font("Helvetica", size=14)
      html = mistletoe.markdown(i)
      print(html)
      pdf.write_html(html, tag_styles={
        #"h3": TextStyle(font_style="B"),
        #"p": TextStyle(color="#ffffff", fill_color="#ffffff")
      })
  pdf.output("parciales.pdf")

def markdownToPDF(md):
  try:
    archivo = open(md, "r", encoding="utf-8")
    text = archivo.read()
    archivo.close()
    html = mistletoe.markdown(text)
    
    pdf = FPDF()
    pdf.add_page()

    pdf.write_html(html)
    pdf.output("parciales.pdf")
  except Exception as e:
    print(e)
