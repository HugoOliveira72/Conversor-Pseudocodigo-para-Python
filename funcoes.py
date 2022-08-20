# Ler arquivo

def readFile():
    with open("entrada.txt", "r", encoding="UTF-8") as file:
        return file.read()


def substituirArquivo(text, find, change):
    return text.replace(find, change)


def gravarArquivo(text):
    with open("saida.txt", "w", encoding="UTF-8") as file:
        file.write(text)


def conveter():
    # ____________________________________ESCREVAL STRING____________________________________#

    # Leitura do arquivo1.2
    texto = readFile()

    #Definição da troca
    procurar = "escreval"
    substituir = "print"


    # Substituição
    textoAlterado = substituirArquivo(texto, procurar, substituir)

    # # ____________________________________ESCREVA STRING____________________________________#

    # Definição da troca
    procurar = 'escreva("'
    substituir = 'print(end=""+"'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)


    # # ____________________________________ESCREVA NOTSTRING____________________________________#

    #Definição da troca
    procurar = 'escreva('
    substituir = 'print(end=""+'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # ____________________________________SE SENAO________________________________#

    # Definição da troca

    procurar = 'senao se'
    substituir = 'elif'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # ____________________________________FIMSE________________________________#

    # # Definição da troca

    procurar = 'fimse'
    substituir = ''

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # ____________________________________SENAO________________________________#

    # Definição da troca

    procurar = 'senao'
    substituir = 'else'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)
    
    # # ____________________________________SE____________________________________#

    # Definição da troca

    procurar = 'se'
    substituir = 'if'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # ____________________________________ENTAO____________________________________#

    # # Definição da troca

    procurar = 'entao'
    substituir = ':'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # ____________________________________PARA________________________________#

    # # Definição da troca

    procurar = 'para'
    substituir = 'for'

    # Substituição
    textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    gravarArquivo(textoAlterado)

# MAIN
conveter()
