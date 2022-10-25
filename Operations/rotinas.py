
def validarFuncao(frase):
    gersu = frase.find("fimprocedimento")
    if (frase.find("fimprocedimento") != -1 or frase.find("fimfuncao") != -1):
        return False
    elif (frase.find("procedimento") != -1 or frase.find("funcao") != -1):   
        return True
    else:
        return False


def rotinas(frase):
    nomeSubRotina = ""
    nova_frase = ""
    parametros = ""
    achouParatenses = False
    parametrosProc = []
    
    if(frase.find("procedimento") != -1):
        nova_frase = frase.replace("procedimento", "")
    else:
        nova_frase = frase.replace("funcao", "")

    # Separar NomeSubRotina e Parametros
    for i in nova_frase:
        if( i == "("  and achouParatenses == False):
            achouParatenses = True
            nomeSubRotina = parametros.strip()
            parametros = ""
        elif (i == ")" and achouParatenses == True):
            parametros += i
            break
        elif (i == "," or i == ":"):
            parametrosProc.append(parametros)
            parametros = ""
        else:
            parametros += i

    parametrosTratados = ""

    # Atribuir parametros a parametros Tratatos
    for j in range(0, len(parametrosProc)):
        if(j < len(parametrosProc) - 1):
            parametrosTratados += parametrosProc[j] + ","
        else:
            parametrosTratados += parametrosProc[j]

    # Montagem do resultado
    result = f"def {nomeSubRotina}({parametrosTratados}):"
    return result