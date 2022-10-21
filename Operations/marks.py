def fixMarks(frase):
    frases = []
    nova_frase = ""
    achou_aspas = False
    qt_aspas = 0

    for i in frase:
        if (i == '\"' and achou_aspas == False and qt_aspas == 0):
            nova_frase += '\"'
            achou_aspas = True
            qt_aspas = 1
        elif (i == '\"' and achou_aspas == True and qt_aspas == 1):
            nova_frase += '\"'
            achou_aspas = False
            qt_aspas = 0
            frases.append(nova_frase)
            frase = frase.replace(nova_frase, "@parametro")
        elif (achou_aspas and qt_aspas == 1):
            nova_frase += i

    return frase, nova_frase
