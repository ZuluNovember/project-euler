def brute_force():
    max = 4_000_000
    evens_sum = 0

    l1 = 1
    l2 = 2
    while l2 <  max:
        if l2 % 2 == 0:
            evens_sum += l2

        l1, l2 = l2, l1 + l2

    return evens_sum

def solution():
    ans = brute_force()
    print(ans)

solution()
