# from Operations.convertCommand import separateWords
from Operations.fileActions import readFileLines


def treatWord(inputWord):
    lines = readFileLines("Docs/","BaseStringExtension")
    for word in lines:
        return inputWord.replace(word," ")
