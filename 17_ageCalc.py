import datetime

def ageCalculator (y,m,d):
    today = datetime.datetime.now().date()
    birthday = datetime.date(y,m,d)
    age = (today-birthday)/365
    return age

age = ageCalculator(1995, 5, 21)
print(age)