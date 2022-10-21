from asyncio.windows_events import NULL
from distutils import text_file
from queue import Empty
from Operations.fileActions import *
from Operations.loopingConverters import LoopingConverter
from Operations.stringExtensions import *

def convertWord():
    
    inputLines = readFileLines("Docs/ConverterBases/","InputBase")
    outputLines = readFileLines("Docs/ConverterBases/","OutputBase")

    LoopingObject = LoopingConverter()
    text = LoopingObject.forConverter()
    
    if text is not None:
        writeExitFile(text)
    else:
        text = readFile("Docs/Files","entrada")

    textLines = readFileLines("Docs/Files/","entrada")

    for j in range(0,len(textLines)):
        for i in range(0, len(inputLines)):
            find = removeNBar(inputLines[i])
            change = removeNBar(outputLines[i])
            textLines[j] = replaceFile(textLines[j], find, change)


    writeStringListExitFile(textLines)

    