from langdetect import detect

text = input("Write a sentence in any language: ")
print(detect(text))
