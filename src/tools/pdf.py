from fpdf import FPDF



def createPDF(dateI,dateF,cont):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, 'Analisis de contaminacion en Madrid', align='C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    text="La siguente grafica muestra la presencia del contaminante {} en el aire de madrid entre las fechas {}-{}-{} y {}-{}-{}. También se muestr el nivel de lluvia en esas mismas fechas."

    pdf.multi_cell(0, 5, text.format(cont,dateI.day,dateI.month,dateI.year,dateF.day,dateF.month,dateF.year),align='L')
    pdf.ln(10)
    pdf.image('../Output/fig.png',w=150,h=100)
    pdf.output('../Output/Analisis_Contaminacion_{}-{}-{}.pdf'.format(dateI.day,dateI.month,dateI.year), 'F')