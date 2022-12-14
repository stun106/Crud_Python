from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

class Relatorios():
    def printClientes(self):
        webbrowser.open("cliente.pdf")
    
    def gerarelatorioCli(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigoEntry.get()
        self.nomeRel = self.NameEntry.get()
        self.TelRel = self.TelEntry.get()
        self.CityRel = self.CityEntry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold",18)
        self.c.drawString(50,700,'Codigo: ')
        self.c.drawString(50,670,'Nome: ')
        self.c.drawString(50,630,'Telefone: ')
        self.c.drawString(50,600,'Cidade: ' )
        
        self.c.setFont("Helvetica",18)
        self.c.drawString(150,700,self.codigoRel)
        self.c.drawString(150,670,self.nomeRel)
        self.c.drawString(150,630,self.TelRel)
        self.c.drawString(150,600,self.CityRel )

        self.c.showPage()
        self.c.save()
        self.printClientes()

