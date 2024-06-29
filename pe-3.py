def smallest_divisor(num):
    i = 2
    while i <= num:
        if num % i == 0:
            return i
        i+=1
    
    return -1
        

# Find all the prime factors from smallest the largest
def solution():
    num = 600851475143
    prime_factors = []

    while num > 1:
        prime_divisor = smallest_divisor(num)
        prime_factors.append(prime_divisor)
        num = num / prime_divisor

    ans = prime_factors.pop()
    print(ans)

solution()