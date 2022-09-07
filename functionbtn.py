from tkinter import*
import sqlite3
from relatorios import Relatorios
class btnfuction(Relatorios):
    #metodo para dar função ao botão 'limpar'
    def limpartela(self):
        self.codigoEntry.delete(0, END)
        self.NameEntry.delete(0, END)
        self.TelEntry.delete(0, END)
        self.CityEntry.delete(0, END)
    
    def conecta_bd(self):                           #<-- metodo que instacializa e conecta a biblioteca sqlite3
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print('conectando..')            #<-- simplificando o uso da conecção 
    
    def desconect(self):                     #<-- metodo para desconectar o banco de dados
        self.conn.close(), print('desconectando..')
    
    def montaTabelas(self):                 #<-- metodo para montar tabelas
        self.conecta_bd(); 
        # criando tabelas
        #types e condições do sqlite3
        self.cursor.execute("""                    
        CREATE TABLE IF NOT EXISTS clientes(                
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
        );
    """)    
        self.conn.commit(); print('banco de dados criado')
        self.desconect()

    def variaveis(self):
        self.codigo = self.codigoEntry.get()
        self.nome = self.NameEntry.get()
        self.telefone = self.TelEntry.get()
        self.cidade = self.CityEntry.get()

    #metodo add cliente
    def addClientes(self):      #<-- usando '.get' para pegar as entry
        self.variaveis()
        self.conecta_bd() #<-- chamando o banco de dados
        #executando o banco de dados
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente,telefone,cidade) 
            VALUES(?,?,?)""",(self.nome,self.telefone,self.cidade)) #<-- para inserir dados as tabelas no banco de dados
        self.conn.commit()      #<-- submetendo
        self.desconect()        #<-- desconectando
        self.selectLista()      #<-- sempre que adicionar o cliente esse metodo atulizara as entry
        self.limpartela()     

    #selecioando a lista de dados
    def selectLista(self):
        self.listaCli.delete(*self.listaCli.get_children()) #<-- assim que adincionar cliente as entry sera apagada
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC""") #<-- ORDER BY + ASC  chamar nome cliente em ordem alfabetica
        for i in lista:             #<-- atualiza a lista sempre que um cliente for adicionado
            self.listaCli.insert("",END,value = i)  #<-- feito isso todos os valores vão ser inseridos na lista do frame2
        self.desconect()

#selecionar com duplo click e mandar para as entry
    def Ondoubleclick(self,event): #<-- sempre que uma função usar um evento sempre adicionar aos paramentros do metodo event
        self.limpartela()
        self.listaCli.selection()

        for n in self.listaCli.selection():             #<-- insere os dados de cada coluna em suas respectivas entry.
            col1,col2,col3,col4 = self.listaCli.item(n,'values')    
            self.codigoEntry.insert(END,col1)
            self.NameEntry.insert(END,col2)
            self.TelEntry.insert(END,col3)
            self.CityEntry.insert(END,col4)

#apagar dados
    def deletaClientes(self):
        self.variaveis()        #<-- chama as entry
        self.conecta_bd()        #<-- conecta o banco de dados
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo,))  #<-- executa o comando
        self.conn.commit()      #<-- submete
        self.desconect()        #<-- desconecta do bd
        self.limpartela()       #<-- limpa os dados
        self.selectLista()

    def alterarClientes(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """, (self.nome,self.telefone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconect()
        self.selectLista()
        self.limpartela()

    def Menus(self):
        menubar = Menu(self.root)   #<-- atribui a função menu com o parametro da class Tk
        self.root.config(menu = menubar)    #<-- configura como menu
        filemenu = Menu(menubar)    #<-- cada variavel sera um menubar
        filemenu2 = Menu(menubar)
        def Quit(): self.root.destroy()
        menubar.add_cascade(label = "Opções", menu= filemenu)   #<-- Cria um nome para cada menu com o "add_cascade"
        menubar.add_cascade(label = "Relatórios", menu = filemenu2)
        filemenu.add_command(label = "sair", command = Quit)        #<-- dentro de cada menu colocamos os comandos com "add_command"
        filemenu.add_command(label = "Limpa Cliente", command = self.limpartela)

        filemenu2.add_command(label = "Ficha do Cliente", command = self.gerarelatorioCli)
        