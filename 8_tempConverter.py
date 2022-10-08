def fahrenheit2celcius (f):
    c = (f-32)*5/9
    return c

text = input("Input temp in Fahrenheit: ")
celcius = fahrenheit2celcius(float(text))
print(celcius)