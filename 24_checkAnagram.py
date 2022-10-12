from tabnanny import check


def checkAnagram (word1, word2):
    anagram = False
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        anagram = True
    return anagram

print(checkAnagram('cinema', 'iceman'))
print(checkAnagram('cool', 'loco'))
print(checkAnagram('men', 'women'))