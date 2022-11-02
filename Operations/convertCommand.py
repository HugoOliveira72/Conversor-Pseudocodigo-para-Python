from Operations.fileActions import *
from Operations.loopingConverters import LoopingConverter
from Operations.marks import fixMarks
from Operations.math import converterMath
from Operations.rotinas import rotinas, validarFuncao
from Operations.read import convertInput
from Operations.stringExtensions import *
from Operations.vetores import convertVetores
from Operations.var import *
from Operations.escolha_caso import *


def convertWord():

    inputLines = readFileLines("Docs/ConverterBases/", "InputBase")
    outputLines = readFileLines("Docs/ConverterBases/", "OutputBase")
    lock = False
    lines = ''
    positionAteLine = 0
    positionRepeatLine = 0
    ateLine = ''
    repeatCurrentText = ''
    entered = 0
    flag = False

    # FOR
    LoopingObject = LoopingConverter()
    text = LoopingObject.forConverter()

    if text is not None:
        writeExitFile(text)
    else:
        text = readFile("Docs/Files", "entrada")

    textLines = readFileLines("Docs/Files/", "entrada")
    currentParameter = ""

    # GERAL
    for j in range(0, len(textLines)):

        # VAR
        textLines[j] = var(textLines[j])

        # Funcoes Matemáticas
        # textLines[j] = converterMath(textLines[j])
        # if j == 0:
        #     textLines.insert(0,"import math\n")
        #     textLines.insert(1,"\n")

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

            # Conversão geral pelos arquivos
            find = removeNBar(inputLines[i])
            change = removeNBar(outputLines[i])
            textLines[j] = replaceFile(textLines[j].strip()+"\n", find, change)

        # Devolver conteudo
        textLines[j] = replaceFile(
            textLines[j], "@parametro", currentParameter)

        # Repita
        if (textLines[j].find('repita') != -1):
            repeatLine, positionRepeatLine = textLines[j], j
            lock = True
        elif (textLines[j].find('ate (') != -1):
            # Chamar Repita e montar
            ateLine, positionAteLine = textLines[j], j
            repeatCurrentText = LoopingObject.repita(ateLine, lines)
            repeatCurrentText = convertToList(repeatCurrentText)

            # Remover linhas do repita
            for i in range(positionAteLine, positionRepeatLine-1, -1):
                del textLines[i]

            initialPosition = positionRepeatLine
            c = 0
            # Ajustar Repita
            for line in repeatCurrentText:
                if line.find('while') != -1:
                    c = initialPosition
                    textLines.insert(initialPosition, line+'\n')
                elif c != 0:
                    textLines.insert(initialPosition, '   '+line+'\n')
                else:
                    textLines.insert(initialPosition, line+'\n')
                initialPosition += 1
        elif lock:
            lines += textLines[j]

        # Escolha - Caso
        if textLines[j].find('escolha') != -1:
            variable = textLines[j].replace('escolha','').strip()
            textLines[j] = escolha(variable, textLines[j], flag)
            entered = 1
        elif entered != 0 and textLines[j].find('caso') != -1:
            textLines[j] = escolha(variable, textLines[j], flag).strip()
            flag = True

    writeStringListExitFile(textLines)
