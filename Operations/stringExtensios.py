# from Operations.convertCommand import separateWords
from Operations.fileActions import readFileLines


def treatWord(inputWord):
    lines = readFileLines("Docs/","BaseStringExtension")
    for word in lines:
        word = word.replace("\n","")
        result = inputWord.replace(word," ")
        return result
        