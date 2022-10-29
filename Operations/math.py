from Operations.stringExtensions import *
from Operations.fileActions import *


def converterMath(texto):
    InputMath = readFileLines("Docs/ConverterBases/Math/", "InputBaseMath")
    OutputMath = readFileLines("Docs/ConverterBases/Math/", "OutputBaseMath")
    result = texto

    for i in range(0, len(InputMath)):
        find = removeNBar(InputMath[i])
        change = removeNBar(OutputMath[i])
        result = replaceFile("math."+result, find, change)

    return result
