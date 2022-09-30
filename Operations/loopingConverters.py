
from Models.Para import Para
from Operations.fileActions import convertToText, readFileLines
from Operations.stringExtensions import removeNBar

def identifyLoopQuantity(self):
    for line in self.textLines:
        if line.find(self.command) != -1:
            self.forLines.append(removeNBar(line))
            self.forLineNumbers.append(lineCounter)
        lineCounter += 1

class LoopingConverter:
    def __init__(self):
        self.textLines = readFileLines("Docs/Files/","entrada")
        self.forBase = ""
        self.forLines = []
        forLineNumbers = []


    def forConverter(self):
        self.command = "para "
        forAtrCounter = 0
        forCounter = 0
        For = Para()

        identifyLoopQuantity()
            
        for actualForLine in self.forLines:
            forAtrCounter = 0
            self.forBase = "for @contador in range(@de, @ate, @passo):"

            for parameter in For.atributes:
                forAtrCounter += 1
        
                
                firstPositionParameterOne = actualForLine.find(parameter)
                lenOfParameter = len(parameter)
                
                # Receber index da primeira posição do parametro 1
                firstPositionParameterOne = firstPositionParameterOne + lenOfParameter if firstPositionParameterOne != -1 else firstPositionParamterTwo 

                if forAtrCounter < For.ForLen:

                    currentAttribute = For.atributes[forAtrCounter]
                    firstPositionParamterTwo = actualForLine.find(currentAttribute)

                    if firstPositionParamterTwo != -1:
                        variable = actualForLine[firstPositionParameterOne+1:firstPositionParamterTwo-1]
                    else:
                        firstPositionParamterTwo = actualForLine.find(For.atributes[forAtrCounter+1])
                        variable = actualForLine[firstPositionParameterOne+1:firstPositionParamterTwo-1]
            
                
                if forAtrCounter == 1:
                    self.forBase = self.forBase.replace(f"@contador",variable)
                else:
                    self.forBase = self.forBase.replace(f"@{parameter}",variable)

                self.textLines[self.forLineNumbers[forCounter]] = self.forBase+"\n"
                    
            forCounter += 1
            
        return convertToText(self.textLines)
    