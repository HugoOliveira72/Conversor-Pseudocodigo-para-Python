from asyncio.windows_events import NULL
from distutils import text_file
from queue import Empty
from Operations.fileActions import *
from Operations.loopingConverters import LoopingConverter
from Operations.marks import fixMarks
from Operations.read import convertInput
from Operations.stringExtensions import *

def convertWord():
    
    inputLines = readFileLines("Docs/ConverterBases/","InputBase")
    outputLines = readFileLines("Docs/ConverterBases/","OutputBase")

    # FOR
    LoopingObject = LoopingConverter()
    text = LoopingObject.forConverter()
    
    if text is not None:
        writeExitFile(text)
    else:
        text = readFile("Docs/Files","entrada")

    textLines = readFileLines("Docs/Files/","entrada")
    currentParameter = ''


    # GENERAL
    for j in range(0,len(textLines)):
        # Aplicar regra das aspas
        textLines[j], currentParameter = fixMarks(textLines[j])
        
        for i in range(0, len(inputLines)):
            #Conversão geral pelos arquivos 
            find = removeNBar(inputLines[i])
            change = removeNBar(outputLines[i])
            textLines[j] = replaceFile(textLines[j], find, change)

            # Conversão de inputs
            if (textLines[j].find("leia") != -1):
                textLines[j] = convertInput(textLines[j])
                break

        # Devolver conteudo 
        textLines[j] = replaceFile(textLines[j],"@parametro",currentParameter)

    writeStringListExitFile(textLines)

    