#body mass index
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

def bmiCalculator(height, weight):
    height = height/100     #conver to m
    bmi = weight/(height**2)
    return bmi

def bmiStatus(bmi):
    if bmi>0:
        if bmi<=16:
            print("You are severely underweight")
        elif bmi<=18.5:
            print("You are underweight")
        elif bmi<=25:
            print("You are healthy")
        elif bmi<=30:
            print("You are overweight")
        else:
            print("You are severely overweight")

bmi = bmiCalculator(height, weight)
status = bmiStatus(bmi)