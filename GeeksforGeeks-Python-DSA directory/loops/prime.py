def find_prime_after(start, max_iterations=100):
        num = start + 1
        iterations = 0

        while iterations < max_iterations:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break  
            if is_prime:
                return num 

            num += 1
            iterations += 1

        return None  
print(find_prime_after(10))  
print(find_prime_after(100, max_iterations=5)) 