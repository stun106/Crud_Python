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

        self.c.showPage()
        self.c.save()
        self.printClientes()

