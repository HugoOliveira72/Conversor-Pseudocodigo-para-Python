frase = "leia(variavel) \n escreval(\"Voce apertiou algo\")"
variavel = ""
nova_frase = frase.replace("leia(", "")
leia = True
for i in nova_frase:
    if(i == ")" and leia):
        leia = False
        variavel += " = input()"
    else:
        variavel += i

print(variavel)