def countChacacter (word):
    count = {}
    for i in word:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

word = 'hola banana'
countChar = countChacacter(word)
print(countChar)