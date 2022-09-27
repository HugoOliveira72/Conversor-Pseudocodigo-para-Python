
from Models.Para import Para
from Operations.fileActions import convertToText, readFileLines
from Operations.stringExtensios import removeNBar


class loopingConverters:
    def __init__(self):
        self.command = "para "
        self.textLines = readFileLines("Docs/Files/","entrada")
        self.forBase = "for @contador in range(@de, @ate, @passo):"
        self.forLines = []

    def forConverter(self):
        lineCounter = 0
        forAtrCounter = 0
        forCounter = 0
        indexLineFor = []

        for line in self.textLines:
            if line.find("para ") != -1:
                self.forLines.append(removeNBar(line))
                indexLineFor.append(lineCounter)
            lineCounter += 1
            
        For = Para()
        for actualForLine in self.forLines:
            for parameter in For.atributes:
                forAtrCounter += 1
        
                indexFoundedParameter = actualForLine.find(parameter)
                lenOfParameter = len(parameter)
                
                if indexFoundedParameter != -1:
                    index = indexFoundedParameter + lenOfParameter
                else :
                    index = value

                if forAtrCounter < For.ForLen:
                    actual_value = For.atributes[forAtrCounter]
                    value = actualForLine.find(actual_value)
                    if value != -1:
                        variable = actualForLine[index+1:value-1]
                    else:
                        value = actualForLine.find(For.atributes[forAtrCounter+1])
                        variable = actualForLine[index+1:value-1]
            
                
                if forAtrCounter == 1:
                    self.forBase = self.forBase.replace(f"@contador",variable)
                else:
                    self.forBase = self.forBase.replace(f"@{parameter}",variable)

                self.textLines[indexLineFor[forCounter]] = self.forBase+"\n"
                    
            forCounter += 1
        return convertToText(self.textLines)
    