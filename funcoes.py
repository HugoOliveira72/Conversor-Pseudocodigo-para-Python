from Operations.convertCommand import convertWord
from Operations.fileActions import *


def converter():

    texto = readFile("","entrada")
    convertWord(texto)
    

converter()
