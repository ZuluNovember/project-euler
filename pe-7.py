def find_prime_numbes(n):
    primes = [2]

    i = 3
    while len(primes) < n:
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(i)

        i += 2

    return primes

def solution():
    limit = 10001
    ans = find_prime_numbes(limit).pop()
    print(ans)

solution()
