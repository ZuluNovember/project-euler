import time
def sum_of_squares_with_formula(num):
    return (2 * num + 1) * (num + 1) * num / 6

def sum_of_squares(num):
    sum = 0

    i = 1
    while i <= num:
        sum += i * i
        i += 1
    
    return sum

def squares_of_sum(num):
    sum = num * (num + 1) / 2

    return sum * sum

def solution():
    limit = 100

    # with loop
    t1 = time.time()
    sum_of_sq = sum_of_squares(limit)
    delta1 = (time.time() - t1) * 1000
    print(f"Sum of squares with loop (ms): {delta1}")

    # with formula
    t2 = time.time()
    sum_of_sq = sum_of_squares_with_formula(limit)
    delta2 = (time.time() - t2) * 1000
    print(f"Sum of squares with formula (ms): {delta2}")

    ans = squares_of_sum(limit) - sum_of_sq

    print(ans)

solution()