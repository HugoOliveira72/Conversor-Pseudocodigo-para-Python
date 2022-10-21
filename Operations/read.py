def convertInput(frase):
    variavel = ""
    nova_frase = frase.replace("leia(", "")
    leia = True
    for i in nova_frase:
        if(i == ")" and leia):
            leia = False
            variavel += " = input()"
        else:
            variavel += i

    # print(variavel)
    return variavel