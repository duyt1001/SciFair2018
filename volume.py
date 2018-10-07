import math
def cv(d,h):
    total = (d/2)**2 * math.pi * h
    return total
    
def locv(d,h,n):
    single = cv(d,h/n)
    total = single*n
    return total

for n in range(1,11):
    print(n,' => ',locv(1,10,n))
