from Operations.fileActions import readFile, readFileLines, replaceFile
from Operations.stringExtensios import treatWord


def separateWords(line):
    counterWords = 0
    w1 = ""
    for word in line.split():
        counterWords += 1
        if counterWords == 1:
            w1 = treatWord(word)
        else:
            w2 = word
    return w1,w2

def convertWord(texto):
    lines = readFileLines("Docs/","Base")
    for line in lines:
        find,change = separateWords(line)
        texto =  replaceFile(texto, find, change)
    
    return texto