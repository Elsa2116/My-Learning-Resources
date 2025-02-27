import heapq

def nthSuperUglyNumber(n, primes):
    heap = []
    seen = set()
    heapq.heappush(heap, 1)
    seen.add(1)
    ugly_number = 1
    
    for _ in range(n):
        ugly_number = heapq.heappop(heap)
    for prime in primes:
            new_ugly = ugly_number * prime
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)
    
    return ugly_number
print(nthSuperUglyNumber(12, [2, 7, 13, 19]))  
print(nthSuperUglyNumber(1, [2, 3, 5]))        