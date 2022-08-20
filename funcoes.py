# Ler arquivo

def readFile():
    with open("entrada.txt", "r", encoding="UTF-8") as file:
        return file.read()


def substituirArquivo(text, find, change):
    return text.replace(find, change)


def gravarArquivo(text):
    with open("entrada.txt", "w", encoding="UTF-8") as file:
        file.write(text)

# ____________________________________ESCREVAL-------------------------------------------#

# Definição da troca
procurar = "escreval"
substituir = "print"

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________ESCREVA-------------------------------------------#

# Definição da troca
procurar = 'escreva("'
substituir = 'print(end=""+"'

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________SE SENAO________________________________#

# Definição da troca

procurar = 'senao se'
substituir = 'elif'

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________FIMSE________________________________#

# Definição da troca

procurar = 'fimse'
substituir = 'else'

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________SE____________________________________#

# Definição da troca

procurar = 'se'
substituir = 'if'

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________ENTAO____________________________________#
# Definição da troca

procurar = 'entao'
substituir = ':'

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________SENAO________________________________#

# Definição da troca

procurar = 'senao'
substituir = 'else'

# Leitura do arquivo1.2
texto = readFile()

# Substituição
textoAlterado = substituirArquivo(texto, procurar, substituir)

# Reescrever o arquivo com as palavras corretas
gravarArquivo(textoAlterado)

# ____________________________________PARA________________________________#
