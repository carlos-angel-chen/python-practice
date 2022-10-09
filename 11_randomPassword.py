import random 

sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+}{|';:/.,?><`~"

passLen = int(input("Enter the lenght of the password: "))

def randomPassword (passLen):
    password = "".join(random.sample(sample,passLen))
    return password

randomPass = randomPassword(passLen)
print(randomPass)