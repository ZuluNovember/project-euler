import time

def isPalindrome(num):
    return str(num) == str(num)[::-1]

def largestPalindrome():
    largestPalindrome = 0
    multiplier = 0

    num = 999
    while num >= 100:
        if num < multiplier:
            return largestPalindrome
        num2 = num
        while num2 >= 100:
            mult = num * num2
            if (isPalindrome(mult) and mult > largestPalindrome):
                print(num, num2)
                largestPalindrome = mult
                multiplier = num2
                break
            num2 -= 1
        num -= 1

    return largestPalindrome




def solution():
    start = time.time()
    ans = largestPalindrome()
    end = time.time()
    print("ans: %d, time: %d", ans, (end -start) * 1000)

solution()