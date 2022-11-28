from enum import Flag
from Operations.stringExtensions import removeNBar, removeTabIdentation


def escolha(variavel, linha, flag):
    condicao = ''
    if linha.find('ortro') != -1:
        linha = 'else:'
    elif linha.find('caso') != -1:
        condicao = linha.replace('caso','')
        condicao = removeNBar(condicao)
        condicao = removeTabIdentation(condicao)
        if flag == True: 
            return f'elif {variavel} == {condicao}:\n'
        return f'if {variavel} == {condicao}:\n'
    elif linha.find('escolha') != -1:
        return '\n'
    return linha+'\n'