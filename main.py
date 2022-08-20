#PALAVRAS JA VALIDADAS
#se, entao, escreva, escreval, fimse
linha =['se 1 > 0 entao\n', 'escreval("rolinha")','senao', 'fimse']
convertido = ''
variavel = ''
variavel_anterior = ''
for conteudo in linha:
    for letra in conteudo:
        #LETRA E
        if(letra == 'e' and variavel == ''):
            variavel += letra
        elif letra == 'e' and variavel == 's':
            variavel += letra
        elif letra == 'e' and variavel == 'escr':
            variavel += letra
        elif letra == 'e' and variavel == 'fims':
            variavel += letra

        #LETRA F
        elif letra == 'f' and variavel == '':
            variavel += letra

        #LETRA S
        elif letra == 's' and variavel == 'e':
            variavel += letra
        elif letra == 's' and variavel == '':
            variavel += letra
        elif(letra == 's' and variavel == 'fim'):
            variavel += letra

        #LETRA C
        elif letra == 'c' and variavel == 'es':
            variavel += letra

        #LETRA R
        elif letra == 'r' and variavel == 'esc':
            variavel += letra

        #LETRA V
        elif letra == 'v' and variavel == 'escre':
            variavel += letra

        #LETRA A
        elif letra == 'a' and variavel == 'escrev':
            variavel += letra
        elif letra == 'a' and variavel == 'ent':
            variavel += letra
        elif letra == 'a' and variavel == 'sen':
            variavel += letra

        #LETRA L
        elif letra == 'l' and variavel == 'escreva':
                variavel += letra

        #LETRA N
        elif letra == 'n' and variavel == 'e':
            variavel += letra
        elif letra == 'n' and variavel == 'se':
            variavel += letra

        #LETRA T
        elif letra == 't' and variavel == 'en':
            variavel += letra

        #LETRA O
        elif letra == 'o' and variavel == 'enta':
            variavel += letra
        elif letra == 'o' and variavel == 'sena':
            variavel += letra

        #LETRA I
        elif letra == 'i' and variavel == 'f':
            variavel += letra

        # LETRA M
        elif letra == 'm' and variavel == 'fi':
            variavel += letra

        # ESPAÇO
        elif letra == ' ' and variavel == 'se':
            if variavel_anterior == 'senao':
                convertido += '\tif '
            else:
                convertido += 'if'
                variavel_anterior = variavel
                variavel = ''
        elif letra == '\n' and variavel == 'entao':
            convertido += ':\n'
            variavel_anterior = variavel
            variavel = ''
        elif(letra == ' ' and variavel == 'fimse'):
            convertido += ''
            variavel_anterior = variavel
            variavel = ''
        elif letra == ' ' and variavel == 'senao':
            convertido += '\nelse:\n '
            variavel_anterior = variavel
            variavel = ''

        # PARENTESES
        elif letra == '(' and variavel == 'escreva':
                if variavel_anterior == 'entao' or variavel_anterior == 'senao':
                    convertido += '\tprint(end=""+'
                else:
                    convertido+= 'print(end=""+'
                    variavel_anterior = variavel
                    variavel = ''
        elif letra == '(' and variavel == 'escreval':
                if variavel_anterior == 'entao' or variavel_anterior == 'senao':
                    convertido += '\tprint('
                else:
                    convertido += 'print('
                    variavel_anterior = variavel
                    variavel = ''

        #PADRAO
        else:
            variavel = ''
            convertido+= letra

print(convertido)

