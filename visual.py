from cgitb import text
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.tix import LabelEntry
from Operations.fileActions import *
from main import Main

class Funcoes():
    def converter(self):
        self.entradaTexto2.delete("1.0", "end")
        writeFile(self.entradaTexto1.get("1.0", 'end-1c'), "Docs/Files", "entrada")
        Main()
        outputFile = readFile("Docs/Files", "saida")
        self.entradaTexto2.insert(INSERT, outputFile)
        showinfo(title='Conversor', message='Convertido')

root = Tk()

class Aplicacao(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.entradas()
        self.botoes()
        self.root.mainloop()

    def tela(self):
        self.root.title("Conversor pseudocodigo")
        self.root.configure(background="#EEE4AB")
        self.root.geometry("1366x768")
        self.root.resizable(True, True)
        self.root.maxsize = "1920x1080"
        self.root.minsizev = "720x480"

    def frames(self):
        self.frame1 = Frame(self.root, bd=4, bg="#99C4C8",
                            highlightbackground="#68A7AD", highlightthickness=3)
        self.frame1.place(relx=0.14, rely=0.13, relwidth=0.3, relheight=0.68)

        self.frame2 = Frame(self.root, bd=4, bg="#99C4C8",
                            highlightbackground="#68A7AD", highlightthickness=3)
        self.frame2.place(relx=0.5, rely=0.13, relwidth=0.3, relheight=0.68)

    def entradas(self):
        self.entradaTexto1 = Text(self.frame1, font="Courier")
        self.entradaTexto1.place(
            relx=0.001, rely=0.001, relwidth=0.999, relheight=0.999)

        self.entradaTexto2 = Text(self.frame2, font="Courier")
        self.entradaTexto2.place(
            relx=0.001, rely=0.001, relwidth=0.999, relheight=0.999)

    def botoes(self):
        self.botaoConverter = Button(root, text="Converter", command=self.converter)
        self.botaoConverter.place(relx=0.46, rely=0.87, relwidth=0.05, relheight=0.05)

Aplicacao()
