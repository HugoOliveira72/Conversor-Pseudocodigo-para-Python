from Operations.fileActions import readFile, substituirArquivo

def convertWord(texto):
    file = open('Docs/Base.txt')
    lines = file.readlines()
    

    # print(lines)
    for line in lines:
        counterWords = 0
        for word in line.split():
            # print(word)
            counterWords += 1
            if counterWords == 1:
                w1 = word
            else:
                w2 = word
        texto =  substituirArquivo(texto, w1, w2)
    
    return texto
