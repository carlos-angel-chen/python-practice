from turtle import right


romanNumbers = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}

def roman2decimal(num):
    sum = 0
    for i in range(len(num)-1):
        left = num[i]
        right = num[i+1]
        if romanNumbers[right]>romanNumbers[left]:
            sum -= romanNumbers[left]
        else: 
            sum += romanNumbers[right]
    sum += romanNumbers[num[-1]]
    return sum

roman = "XXL"
result = roman2decimal(roman)
print(result)