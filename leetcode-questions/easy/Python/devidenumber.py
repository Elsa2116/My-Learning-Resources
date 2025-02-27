def countDividingDigits(num):
    original_num = num  
    count = 0  
    
    while num > 0:
        digit = num % 10  
        if original_num % digit == 0:  
            count += 1  
        num //= 10  
    return count
print(countDividingDigits(7))    
print(countDividingDigits(121))  
print(countDividingDigits(1248)) 