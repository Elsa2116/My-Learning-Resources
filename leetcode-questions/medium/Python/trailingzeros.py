def trailingZeroes(n):
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
        
    return count
print(trailingZeroes(3))   
print(trailingZeroes(5))   
print(trailingZeroes(0))   
print(trailingZeroes(10))  
print(trailingZeroes(25))  