
from Models.Enquanto import Enquanto
from Models.Para import Para
from Operations.fileActions import convertToText, readFileLines
from Operations.stringExtensios import removeLastCaracter, removeNBar


class loopingConverters:
    def __init__(self):
        self.command = "para "
        self.textLines = readFileLines("","entrada")
        self.forBase = "for @contador in range(@de, @ate, @passo):"
        self.text = ""

    def forConverter(self):
        lineCounter = 0
        forCounter = 0

        for line in self.textLines:
            if line.find("para") != -1:
                self.text = removeNBar(line)
                break
            lineCounter += 1

        For = Para()
        for parameter in For.atributes:
            forCounter += 1
    
            index = self.text.find(parameter) + len(parameter)

            if forCounter < For.ForLen:
                actual_value = For.atributes[forCounter]
                value = self.text.find(actual_value[:-1])
                variable = self.text[index+1:value-1]
            
            if forCounter == 1:
                self.forBase = self.forBase.replace(f"@contador",variable)
            else:
                self.forBase = self.forBase.replace(f"@{parameter}",variable)
                
        self.textLines[lineCounter] = self.forBase+"\n"
        return convertToText(self.textLines)
    
    # def whileConverter(self):
        lineCounter = 0
        forCounter = 0

        for line in self.textLines:
            if line.find("para") != -1:
                self.text = removeNBar(line)
                break
            lineCounter += 1

        While = Enquanto()
        for parameter in While.atributes:
            forCounter += 1
            index = self.text.find(parameter) + len(parameter)

            if forCounter < While.ForLen:
                actual_value = While.atributes[forCounter]
                value = self.text.find(actual_value[:-1])
                variable = self.text[index+1:value-1]
            
            if forCounter == 1:
                self.forBase = self.forBase.replace(f"@contador",variable)
            else:
                self.forBase = self.forBase.replace(f"@{parameter}",variable)
                
        self.textLines[lineCounter] = self.forBase+"\n"
        return convertToText(self.textLines)