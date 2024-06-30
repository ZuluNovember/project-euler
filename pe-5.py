def least_common_multiple(max):
    result = 1
    numbers = list(range(1,21))

    i = 2
    while i <= max:
        done = True
        for idx, val in enumerate(numbers):
            if val % i == 0:
                numbers[idx] = val / i
                done = False

        if done:
            i+=1
        else:
            result = result * i

    return result

def solution():
    ans = least_common_multiple(20)
    print(ans)

solution()