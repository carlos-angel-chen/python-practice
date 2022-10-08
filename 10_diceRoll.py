import random

min = 1
max = 6 

keepRoll = "yes"

while (keepRoll=="yes" or keepRoll=="y"):
    print("The value is: ")
    randomNum = random.randint(min, max)
    print(randomNum)
    keepRoll = input("Do you want to keep rolling? ")
