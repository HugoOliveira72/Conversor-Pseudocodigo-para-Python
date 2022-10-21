frase = "escreval(\"escreval mundo odeia o crhis\")"
frases = []
nova_frase = ""
achou_aspas = False
qt_aspas = 0

for i in frase:
    if(i == '\"' and achou_aspas == False and qt_aspas == 0):
        nova_frase += '\"'
        achou_aspas = True
        qt_aspas = 1
    elif(i == '\"'and achou_aspas == True and qt_aspas == 1):
        nova_frase += '\"'
        achou_aspas = False
        qt_aspas = 0
        frases.append(nova_frase)
        frase = frase.replace(nova_frase, "@parametro")
    elif(achou_aspas and qt_aspas == 1):
        nova_frase += i

print("frase sem tratativas")
print(frase)
print("frase que ira substituir a palavra  @parametro")
print(nova_frase)
print("convertendo codigo")
frase = frase.replace("escreval", "printf")
print("depois de converter")
print(frase)
print("substituindo parametro")
frase = frase.replace("@parametro", nova_frase)
print("frase depois de convertida")
print(frase)


frases.append(nova_frase)
index1 = len(frases)
print(f"@parametro{(index1 - 1)}" )