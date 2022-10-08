def checkPalindrome(sentence):
    check = False
    #replace every special character form the sentence
    specialChar = [",","."," ",":",";","-"]
    for i in sentence:
        if i in specialChar:
            sentence = sentence.replace(i,"")
    
    #check if it is even or odd
    if len(sentence)%2 == 0:    #its even
        count = len(sentence)/2
        reverseCount = 1
        checkCount = 0
        for i in range(int(count)):
            if sentence[i]!=sentence[i-reverseCount]:
                break
            else:
                reverseCount+=2
                checkCount+=1
        if checkCount==int(count):
            check = True
    else:                       #its odd
        count = len(sentence)/2
        reverseCount = 1
        checkCount = 0
        for i in range(int(count)):
            if sentence[i]!=sentence[i-reverseCount]:
                break
            else:
                reverseCount+=2
                checkCount+=1
        if checkCount==int(count):
            check = True

    return check

sentenceOdd = "a luna, ese anula"
sentenceEven = "amar - rama"
sentence = "hola loco"
palindromeOdd = checkPalindrome(sentenceOdd)
palindromeEven = checkPalindrome(sentenceOdd)
palindromeNot = checkPalindrome(sentence)
print(palindromeOdd)
print(palindromeEven)
print(palindromeNot)