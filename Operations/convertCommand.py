from distutils import text_file
from Operations.fileActions import *
from Operations.loopingConverters import loopingConverters
from Operations.stringExtensios import *

def convertWord():
    
    inputLines = readFileLines("Docs/ConverterBases/","InputBase")
    outputLines = readFileLines("Docs/ConverterBases/","OutputBase")

    LoopingObject = loopingConverters()
    text = LoopingObject.forConverter()
    
    writeExitFile(text)

    for i in range(0, len(inputLines)):
        find = removeNBar(inputLines[i])
        change = removeNBar(outputLines[i])
        text = replaceFile(text, find, change)

    writeExitFile(text)

    