#!/usr/bin/python3
# __autor__ == '__Ivanoel__'
# https://www.github.com/ivanoel

from tkinter import *

main = Tk()

main.geometry('480x320')

main.title('Emulador do Super Nitendo')

def hello():
#    lebel['text'] = salut.get()
     sys.exit()   
def arq():
    abrir = filedialog.askopenfilename(title = "Abrir")
    abrir.start() # erro
    
def Conf():
    sys.exit()

def quit():
     print("O Emulador foi criado com intuito\n de satisfazer minha necessidade de \njogos kkk versão 1.0")
	

# Criando o menu do emulador

menu = Menu(main)
sousmenu = Menu(menu, tearoff=0)
sousmenu2 = Menu(menu, tearoff=0)
sousmenu3 = Menu(menu, tearoff=0)
sousmenu4 = Menu(menu, tearoff=0)

menu.add_cascade(label="Menu", menu=sousmenu)
sousmenu.add_command(label="Iniciar", command=Menu)
sousmenu.add_command(label="Reiniciar", command=Menu)
sousmenu.add_command(label="CD-Rom", command=Menu)
sousmenu.add_command(label="Iso", command=Menu)
sousmenu.add_command(label="Sair", command=Menu)



menu.add_cascade(label="Arquivos",menu=sousmenu2)
sousmenu2.add_command(label="Abrir", command=arq)
sousmenu2.add_command(label="Salve", command=arq)
sousmenu2.add_command(label="Load", command=arq)
sousmenu2.add_command(label="Reset", command=arq)

menu.add_cascade(label="Configurações", menu=sousmenu3)
sousmenu3.add_command(label="Bios", command=Conf)
sousmenu3.add_command(label="Video", command=Conf)
sousmenu3.add_command(label="Audio", command=Conf)
sousmenu3.add_command(label="Controle", command=Conf)
sousmenu3.add_command(label="Memory Card", command=Conf)

menu.add_cascade(label="Sobre", menu=sousmenu4)
sousmenu4.add_command(label="About", command=quit)

# Inserindo uma foto no plano de fundo.

photo = PhotoImage(file="python2.png")
img = Label(main, image = photo).pack()


main.config(menu = menu)
