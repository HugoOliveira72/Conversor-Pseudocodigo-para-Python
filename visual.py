from tkinter import *
from tkinter.messagebox import showinfo

from matplotlib.pyplot import text
import funcoes


def Converter_Clicked():
    texto2.delete("1.0","end")
    funcoes.gravarArquivo(texto1.get("1.0",'end-1c'))
    funcoes.Conveter()
    texto2.insert(INSERT, funcoes.readFile())
    showinfo(title='Conversor',message='Convertido')

janela = Tk()
janela.title("Conversor pseudocodigo")
janela.configure(bg="#b8c4ed")
janela.geometry("1366x768")

tituloJanela = Label(janela,text='Bem vindo ao conversor de pseudcódigo!',bg="#b8c4ed",font="Arial",fg="Blue")
tituloJanela.grid(row=0,column=6)

vazio = Label(janela,text='                ',bg="#b8c4ed",font="Arial",fg="Blue")
vazio.grid(row=0,column=1)
titulotexto1 = Label(janela,text='Pseudocódigo',bg="#b8c4ed",font="Arial",fg="Blue")
titulotexto1.grid(row=2,column=2)
texto1 = Text(janela,height=30,width=50, font="Arial")
texto1.grid(row=3,column=2)

titulotexto2 = Label(janela,text='Python',bg="#b8c4ed",font="Arial",fg="Blue")
titulotexto2.grid(row=2,column=12)
texto2 = Text(janela,height=30,width=50, font="Arial")
texto2.grid(row=3,column=12)

botao = Button(janela,text="Converter", bg="Blue",fg="white",height=3,width=10,command=Converter_Clicked)
botao.grid(row=5,column=6)

janela.mainloop()