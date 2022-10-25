
frase = 'procedimento soma(a,b: inteiro)\nvar\ninicio\nescreval(a+b)\nfimprocedimento\nalgoritmo "A11Ex03"\nvar\nvariable1, variable2: inteiro\ninicio\nleia(variable1)\nleia(variable2)\nsoma(variable1,variable2)\nfimalgoritmo'

nomeSubRotina = ""
nova_frase = frase.replace("procedimento", "")
parametros = ""
achouParatenses = False
parametrosProc = []

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

for j in range(0, len(parametrosProc)):
    if(j < len(parametrosProc) - 1):
        parametrosTratados += parametrosProc[j] + ","
    else:
        parametrosTratados += parametrosProc[j]

result = f"def {nomeSubRotina}({parametrosTratados}):"