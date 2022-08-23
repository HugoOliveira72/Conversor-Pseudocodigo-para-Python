from Operations.fileActions import readFile, readFileLines, replaceFile
from Operations.stringExtensios import treatWord

def convertWord(texto):
    inputLines = readFileLines("Docs/ConverterBases/","InputBase")
    outputLines = readFileLines("Docs/ConverterBases/","OutputBase")

    for i in range(0, len(inputLines)):
        find = treatWord(inputLines[i])
        change = treatWord(outputLines[i])
        texto = replaceFile(texto, find, change)
    return texto
