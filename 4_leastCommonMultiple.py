def leastCommonMultiple(a,b):
    if a>b:
        greater = a
    elif a<b:
        greater = b
    
    check = True
    while(check):
        if ((greater%a == 0) and (greater%b == 0)):
            check = False
        else:
            greater+=1
    
    return greater

lcm = leastCommonMultiple(12, 15)
print(lcm)