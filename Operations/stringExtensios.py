# from Operations.convertCommand import separateWords
from Operations.fileActions import readFileLines


def removeNBar(input):
    return input.replace("\n","")

def addNBar(input):
    return input+"\n"

def removeLastCaracter(input):
    return input[:-1]