import math
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def isThree(n):
    root = int(math.sqrt(n))
    return root * root == n and is_prime(root)
print(isThree(2))  
print(isThree(4))  
print(isThree(9))  
print(isThree(10)) 