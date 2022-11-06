from importlib.metadata import files


def readFile(path, filename):
    with open(f"{path}/{filename}.txt", "r", encoding="UTF-8") as file:
        return file.read()


def replaceFile(text, find, change):
    return text.replace(find, change)


def writeExitFile(text):
    with open("Docs/Files/saida.txt", "w", encoding="UTF-8") as file:
        file.write(text)


def writeStringListExitFile(lines):
    text = ''
    for line in lines:
        text += line
    writeExitFile(text)


def writeFile(text, path, filename):
    with open(f"{path}/{filename}.txt", "w", encoding="UTF-8") as file:
        file.write(text)


def readFileLines(path, filename):
    file = open(f'{path}{filename}.txt',encoding='utf-8')
    lines = file.readlines()
    return lines


def convertToText(lines):
    texto = ""
    for line in lines:
        texto += line
    return texto

def convertToList(text):
    lines = []
    res = ''
    for palavra in text:
        if palavra != '\n':
            res += palavra
        else:
            lines.append(res)
            res = ''

    return lines        
