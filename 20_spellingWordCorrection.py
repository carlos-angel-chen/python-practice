from traceback import print_tb
from textblob import TextBlob

def conver2list(string):
    listWord = list(string.split())
    return listWord

def wordCorrection(listOfWord):
    correctedWord = []
    for i in listOfWord:
        correctedWord.append(TextBlob(i))
    return correctedWord

wrongWords = input("Enter wrong words: ")
listOfWrongWords = conver2list(wrongWords)
correctWords = wordCorrection(listOfWrongWords)
for i in correctWords:
    print(i.correct(), end=' ')