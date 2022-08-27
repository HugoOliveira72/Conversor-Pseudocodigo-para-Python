file = open('Tests/text.txt')
lines = file.readlines()
texto = lines[0]
        
index1 = texto.find("para ") + len("para ")
Variavel_Contador = texto[index1]
index2 = texto.find("de ") + len("de ")
De = texto[index2]
index3 = texto.find("ate ") + len("ate ")
Ate = texto[index3]
index4 = texto.find("passo ") + len("passo ")
Passo = texto[index4]


for_ = "for @contador in range(@de,  @ate,  @passo)"
texto = for_.replace("@contador", Variavel_Contador)
texto = texto.replace("@de", De)
texto = texto.replace("@ate", Ate)
texto = texto.replace("@passo", Passo)
print(texto)
lines[0] = texto
print(lines)