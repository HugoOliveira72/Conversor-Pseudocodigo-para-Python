from Operations.convertCommand import convertWord
from Operations.fileActions import *


def converter():
    # ____________________________________ESCREVAL STRING____________________________________#

    # Leitura do arquivo1.2
    texto = readFile('','entrada')
    textoAlterado = convertWord(texto)

    #Definição da troca
    

    # # # ____________________________________ESCREVA STRING____________________________________#

    # # Definição da troca
    # procurar = 'escreva("'
    # substituir = 'print(end=""+"'

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)


    # # # ____________________________________ESCREVA NOTSTRING____________________________________#

    # #Definição da troca
    # procurar = 'escreva('
    # substituir = 'print(end=""+'

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # # ____________________________________SE SENAO________________________________#

    # # Definição da troca

    # procurar = 'senao se'
    # substituir = 'elif'

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # # ____________________________________FIMSE________________________________#

    # # # Definição da troca

    # procurar = 'fimse'
    # substituir = ''

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # ____________________________________SENAO________________________________#

    # # Definição da troca

    # procurar = 'senao'
    # substituir = 'else'

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)
    
    # # # ____________________________________SE____________________________________#

    # # Definição da troca

    # procurar = 'se'
    # substituir = 'if'

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    # # # ____________________________________ENTAO____________________________________#

    # # # Definição da troca

    # procurar = 'entao'
    # substituir = ':'

    # # Substituição
    # textoAlterado = substituirArquivo(textoAlterado, procurar, substituir)

    writeFile(textoAlterado)

converter()