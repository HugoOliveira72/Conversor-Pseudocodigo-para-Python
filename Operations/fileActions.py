def readFile(path,filename):
    with open(f"{path}{filename}.txt", "r", encoding="UTF-8") as file:
        return file.read()

def replaceFile(text, find, change):
    return text.replace(find,change)

def writeFile(text):
    with open("Docs/Files/saida.txt", "w", encoding="UTF-8") as file:
        file.write(text)

def readFileLines(path,filename):
    file = open(f'{path}{filename}.txt')
    lines = file.readlines()
    return lines

def convertToText(lines):
    texto = ""
    for line in lines:
        texto += line
    return texto