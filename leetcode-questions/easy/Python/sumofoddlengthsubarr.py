def sumOddLengthSubarrays(arr):
    n = len(arr)
    total_sum = 0
    
    for i in range(n):
        total_subarrays = (i + 1) * (n - i)
    odd_count = (total_subarrays + 1) // 2
        
    total_sum += arr[i] * odd_count
    
    return total_sum

print(sumOddLengthSubarrays([1, 4, 2, 5, 3]))  
print(sumOddLengthSubarrays([1, 2]))            
print(sumOddLengthSubarrays([10, 11, 12]))      