from Operations.fileActions import readFileLines, replaceFile, writeFile
from Operations.loopingConverters import loopingConverters
from Operations.stringExtensios import *

def convertWord(texto):
    inputLines = readFileLines("Docs/ConverterBases/","InputBase")
    outputLines = readFileLines("Docs/ConverterBases/","OutputBase")

    for i in range(0, len(inputLines)):
        find = removeNBar(inputLines[i])
        change = removeNBar(outputLines[i])
        texto = replaceFile(texto, find, change)
    
    writeFile(texto)
        
    LoopingObject = loopingConverters()
    writeFile(LoopingObject.forConverter())

    