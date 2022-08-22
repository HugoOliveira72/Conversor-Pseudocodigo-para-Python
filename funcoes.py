from Operations.convertCommand import convertWord
from Operations.fileActions import *


def converter():

    texto = readFile("","entrada")
    textoAlterado = convertWord(texto)
    
    writeFile(textoAlterado)

converter()
