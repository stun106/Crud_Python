from tkinter import*
from tkinter import ttk
from functionbtn import btnfuction

root = Tk()

class App(btnfuction):                                     
    def __init__(self):
        self.root = root              #<-- instancia de class  
        self.tela()         #<-- Configuração e estilização da tela e seus componentes
        self.framesdaTela()
        self.Widgets_frame1()
        self.listaFrame2()
        self.montaTabelas()
        self.selectLista()
        self.Menus()
        root.mainloop() # <-- metodo para dar retorno a tela

    def tela(self):
        self.root.title('Cadastro de Clientes')         
        self.root.configure(background='#1e3743')       #<-- background da tela + cor
        self.root.geometry('700x500')               #<-- definindo tamanho 
        self.root.resizable(True,True)              #<-- responsividade de acordo com eixos
        self.root.maxsize(width=1080,height=720)                #<-- predeterminando largura maxima
        self.root.minsize(width=600,height=500)

    def framesdaTela(self):
        self.frame1 = Frame(
            self.root,bd = 2, bg = '#dfe3ee',
            highlightbackground = '#759fe6', highlightthickness = 3         #<-- Função 'Frame' para atribuir a class mãe e usar parametros de cusmização e etc..
        )   
        self.frame2 = Frame(
            self.root,bd = 2, bg = '#dfe3ee',
            highlightbackground = '#759fe6', highlightthickness = 3
        )
        
        self.frame1.place(relx = 0.02,rely = 0.02, relwidth = 0.96, relheight = 0.46)   #<-- Função 'place' para criar o frame, seus parametros atribui valores com posições relativas ou absolutas; porcentagem para relativas e inteiro para absoluta. 
        self.frame2.place(relx = 0.02,rely = 0.5, relwidth = 0.96, relheight = 0.46)
    
    def Widgets_frame1(self):
        #Botão de limpar
        self.btn_Clear = ttk.Button(self.frame1,text = 'Limpar', command= self.limpartela)
        self.btn_Clear.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight=0.15)
        #botão de Buscar
        self.btn_Search = ttk.Button(self.frame1, text= 'Buscar')
        self.btn_Search.place(relx = 0.3, rely = 0.1, relwidth = 0.1, relheight=0.15 )
        #botão de novo
        self.btn_Novo = ttk.Button(self.frame1, text= 'Adicionar', command = self.addClientes)
        self.btn_Novo.place(relx = 0.6, rely = 0.1, relwidth = 0.1, relheight=0.15 )
        #botão de alterar
        self.btn_Alterar = ttk.Button(self.frame1, text= 'Alterar', command = self.alterarClientes)
        self.btn_Alterar.place(relx = 0.7, rely = 0.1, relwidth = 0.1, relheight=0.15 )
        #botão de apagar
        self.btn_Apagar = ttk.Button(self.frame1, text= 'Apagar', command = self.deletaClientes)
        self.btn_Apagar.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight=0.15 )
    
        #Label e entrada do codigo
        self.lbCodigo = Label(self.frame1, text = 'Código',bg = '#dfe3ee')
        self.lbCodigo.place(relx = 0.05, rely = 0.05)
        self.codigoEntry = Entry(self.frame1)
        self.codigoEntry.place(relx = 0.05, rely = 0.15, relwidth = 0.08)
        #Label e entrada do nome
        self.lbName = Label(self.frame1, text = 'Nome',bg = '#dfe3ee')
        self.lbName.place(relx = 0.05, rely = 0.35)
        self.NameEntry = Entry(self.frame1)
        self.NameEntry.place(relx = 0.05, rely = 0.45, relwidth = 0.8)
         #Label e entrada do telefone
        self.lbTel = Label(self.frame1, text = 'Telefone',bg = '#dfe3ee')
        self.lbTel.place(relx = 0.05, rely = 0.6)
        self.TelEntry = Entry(self.frame1)
        self.TelEntry.place(relx = 0.05, rely = 0.7, relwidth = 0.4)
        #Label e entrada do cidade
        self.lbCity = Label(self.frame1, text = 'Cidade',bg = '#dfe3ee')
        self.lbCity.place(relx = 0.5, rely = 0.6)
        self.CityEntry = Entry(self.frame1)
        self.CityEntry.place(relx = 0.5, rely = 0.7, relwidth = 0.4)
    
    def listaFrame2(self):
        #Lista de cadastro 
        self.listaCli = ttk.Treeview(self.frame2, height = 3,columns = ('col1','col2','col3','col4'))   #<-- usando a class ttk e atribuindo a função Treeview para contruir 4 colunas
        # Cabeçalho da lista
        self.listaCli.heading('#0',text ='')    
        self.listaCli.heading('#1', text = 'Código')                               
        self.listaCli.heading('#2', text = 'Nome')
        self.listaCli.heading('#3', text = 'Telefone')
        self.listaCli.heading('#4', text = 'Cidade')
        # usando a função column, o primeiro parametro representa a posição e o segundo a largura, o valor do tamanho de cada coluna se refere ao cabeçalho e sua largura e dividia por 500
        self.listaCli.column('#0',width = 1)
        self.listaCli.column('#1',width = 50)
        self.listaCli.column('#2',width = 200)
        self.listaCli.column('#3',width = 125)
        self.listaCli.column('#4',width = 125)
        self.listaCli.place(relx = 0.01, rely = 0.1, relwidth = 0.95, relheight = 0.85 )
        #'Scrollbar' para criar uma barra de rolagem onde vai ser atribuida a lista
        self.scroollista = Scrollbar(self.frame2, orient = 'vertical')
        self.listaCli.configure(yscrol = self.scroollista.set)
        self.scroollista.place(relx = 0.96,rely = 0.1, relwidth = 0.04, relheight = 0.85)
        self.listaCli.bind("<Double-1>", self.Ondoubleclick)

App()