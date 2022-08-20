def readFile(path,filename):
    with open(f"{path}{filename}.txt", "r", encoding="UTF-8") as file:
        return file.read()

def substituirArquivo(text, find, change):
    return text.replace(find, change)

def gravarArquivo(text):
    with open("saida.txt", "w", encoding="UTF-8") as file:
        file.write(text)