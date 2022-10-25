from unittest import TextTestResult
from Operations.fileActions import *
from Operations.loopingConverters import LoopingConverter
from Operations.marks import fixMarks
from Operations.rotinas import rotinas, validarFuncao
from Operations.read import convertInput
from Operations.stringExtensions import *
from Operations.vetores import convertVetores

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
    currentParameter = ""

    # GENERAL
    for j in range(0,len(textLines)):
        
        # Funcoes
        if (validarFuncao(textLines[j])):
            textLines[j] = rotinas(textLines[j])

        # Vetores / Matrizes
        if (textLines[j].find("vetor") != -1):
            textLines[j] = convertVetores(textLines[j])

        # Conversão de inputs
        if (textLines[j].find("leia") != -1):
            textLines[j] = convertInput(textLines[j])

        # Aplicar regra das aspas
        textLines[j], currentParameter = fixMarks(textLines[j])

        # CONVERSÃO
        for i in range(0, len(inputLines)):

            #Conversão geral pelos arquivos 
            find = removeNBar(inputLines[i])
            change = removeNBar(outputLines[i])
            textLines[j] = replaceFile(textLines[j].strip()+"\n", find, change)

        # Devolver conteudo 
        textLines[j] = replaceFile(textLines[j],"@parametro",currentParameter)

    writeStringListExitFile(textLines)

    