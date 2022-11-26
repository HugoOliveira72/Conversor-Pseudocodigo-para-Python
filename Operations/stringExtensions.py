# from Operations.convertCommand import separateWords

def removeNBar(input):
    return input.replace("\n", "")


def addNBar(input):
    return input+"\n"


def removeLastCaracter(input):
    return input[:-1]


def removeTabIdentation(linha):
    resultLine = ''
    for caracter in linha:
        if caracter != ' ':
            resultLine += caracter

    return resultLine
