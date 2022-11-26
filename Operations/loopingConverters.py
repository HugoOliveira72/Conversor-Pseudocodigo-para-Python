
from Models.Para import Para
from Operations.fileActions import convertToText, readFileLines, replaceFile
from Operations.stringExtensions import removeNBar


def identifyLoopQuantity(self):
    lineCounter = 0
    for line in self.textLines:
        if line.find(self.command) != -1:
            self.forLines.append(removeNBar(line))
            self.forLineNumbers.append(lineCounter)
        lineCounter += 1


class LoopingConverter:
    def __init__(self):
        self.textLines = readFileLines("Docs/Files/", "entrada")

        # FOR
        self.forBase = ""
        self.forLines = []
        self.forLineNumbers = []

    def forConverter(self):
        self.command = "para "
        forAtrCounter = 0
        forCounter = 0
        For = Para()

        identifyLoopQuantity(self)

        for actualForLine in self.forLines:
            forAtrCounter = 0
            self.forBase = "for @contador in range(@de, @ate, @passo):"

            for parameter in For.atributes:
                forAtrCounter += 1

                firstPositionParameterOne = actualForLine.find(parameter)
                lenOfParameter = len(parameter)

                # Receber index da primeira posição do parametro 1
                firstPositionParameterOne = firstPositionParameterOne + \
                    lenOfParameter if firstPositionParameterOne != -1 else firstPositionParamterTwo

                if forAtrCounter < For.ForLen:

                    # Receber index da primeira posição do parametro 2
                    currentAttribute = For.atributes[forAtrCounter]
                    firstPositionParamterTwo = actualForLine.find(
                        currentAttribute)

                    # Atribuição dos valores a uma variavel
                    if firstPositionParamterTwo != -1:
                        variable = actualForLine[firstPositionParameterOne +
                                                 1:firstPositionParamterTwo-1]
                    else:
                        firstPositionParamterTwo = actualForLine.find(
                            For.atributes[forAtrCounter+1])
                        variable = actualForLine[firstPositionParameterOne +
                                                 1:firstPositionParamterTwo-1]

                # Substituição no arquivo
                if forAtrCounter == 1:
                    self.forBase = self.forBase.replace(f"@contador", variable)
                else:
                    self.forBase = self.forBase.replace(
                        f"@{parameter}", variable)

                self.textLines[self.forLineNumbers[forCounter]
                               ] = self.forBase+"\n"

            forCounter += 1

        return convertToText(self.textLines)

    def repita(self, ate, linhas):
        result = ''

        ate = ate.replace('ate','while')
        ate = ate.replace('==','<=')
        ate += ':\n'
        result = linhas
        result += ate

        result += linhas
        return result
        
a = LoopingConverter()
