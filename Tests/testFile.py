
# para i de 1 ate 10 passo 1 faca:
#      escreval(i)
# fimpara

# for i in range(0,1,1):
#     print(i)



# def Metodo(Variavel_Contador, De, Ate, Passo):
#     print('')

# def ChamarMetodo():
#     Index = File.Find("para ")
#     Metodo(file.Find())


texto = ("para i de 1 ate 5 passo 9 faca:" +
            "\nescreval(i)" +
        "\nfimpara")
index = texto.find("para ") + len("para ") - 1
Variavel_Contador = texto[index + 1]
index = texto.find("de ") + len("de ") - 1
De = texto[index + 1]
index = texto.find("ate ") + len("ate ") - 1
Ate = texto[index + 1]
index = texto.find("passo ") + len("passo ") - 1
Passo = texto[index + 1]

for_ = "for @contador in range(@de,  @ate,  @passo)"
resultado = for_.replace("@contador", Variavel_Contador)
resultado = resultado.replace("@de", De)
resultado = resultado.replace("@ate", Ate)
resultado = resultado.replace("@passo", Passo)
print(resultado)


