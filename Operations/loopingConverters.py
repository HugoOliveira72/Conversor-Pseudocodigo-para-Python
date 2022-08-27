
from cgitb import text
from distutils import text_file
from Operations.fileActions import convertToText, readFileLines


class loopingConverters:
    def __init__(self):
        self.command = "para "
        self.textLines = readFileLines("","saida")
        self.text = ""

        print('lau')
        # self.text = texto

    def forConverter(self):
        lineCounter = 0

        for line in self.textLines:
            if line.find("para") != -1:
                self.text = line
                break
            lineCounter += 1
            

        index1 = self.text.find("para ") + len("para ")
        Variavel_Contador = self.text[index1]
        index2 = self.text.find("de ") + len("de ")
        De = self.text[index2]
        index3 = self.text.find("ate ") + len("ate ")
        Ate = self.text[index3]
        index4 = self.text.find("passo ") + len("passo ")
        Passo = self.text[index4]

        for_ = "for @contador in range(@de,  @ate,  @passo)"
        self.text = for_.replace("@contador", Variavel_Contador)
        self.text = self.text.replace("@de", De)
        self.text = self.text.replace("@ate", Ate)
        self.text = self.text.replace("@passo", Passo)

        self.textLines[lineCounter] = self.text
        return convertToText(self.textLines)
        