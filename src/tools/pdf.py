from fpdf import FPDF



def createPDF(date):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Analisis de contaminacion en Madrid')
    pdf.image('fig.png',15,20)
    pdf.output('../Output/Analisis_Contaminacion_{}-{}-{}.pdf'.format(date.day,date.month,date.year), 'F')