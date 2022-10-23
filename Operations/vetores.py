from gettext import find

def convertVetores(frase):
    texto = ""
    variavel = ""
    achou_colchetes = False
    qtd_colchetes = 0

    # Pegar nome da variavel 
    # Pegar o tamanho do vetor/matriz
    for i in frase:
        if(i == ":"):
            variavel = texto
            texto = ""
        elif(i == "[" and achou_colchetes == False and qtd_colchetes == 0):
            achou_colchetes = True
            qtd_colchetes = 1
            texto = ""
        elif(i == "]" and achou_colchetes == True and qtd_colchetes == 1):
            achou_colchetes = False
            tamanho = texto
            variavel += ":"
            break
        else:
            texto += i

    tamanhoVetores = []
    tamanho = tamanho.replace("1..","")

    # Adicionar os tamanhos dos vetores
    for i in tamanho:
        if (i != "," and i != " "):
            tamanhoVetores.append(int(i))
    
    # Preencher vetor/matriz com zeros
    for i in range(0 , len(tamanhoVetores)):

        for j in range(0, tamanhoVetores[i]):
            if (j == 0):
                variavel += " [0"
            elif (j == tamanhoVetores[i]-1):
                variavel += ",0]"
            else:
                variavel += ",0"

        if (len(tamanhoVetores) > 1 and i < len(tamanhoVetores)-1):
            variavel += ","

    return variavel
