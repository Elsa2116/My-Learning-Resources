def isUgly(n):
    if n <= 0:
        return False  
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    return n == 1
print(isUgly(6))   
print(isUgly(1))   
print(isUgly(14))  