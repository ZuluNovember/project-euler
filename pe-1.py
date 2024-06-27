def findLargestDivisible(number, denominator):
    while number > 0:
        if number % denominator == 0:
            return number
        number -= 1

    return 0

def sum_range_with_increment(endNum, increment):
    return endNum * (endNum + increment) / (2 * increment)

def solution():
    countTo = 999
    multiplesOf3 = sum_range_with_increment(findLargestDivisible(countTo, 3), 3)
    multiplesOf5 = sum_range_with_increment(findLargestDivisible(countTo, 5), 5)

    # Multiples of 15 is counted twice, remove one
    multiplesOf15 = sum_range_with_increment(findLargestDivisible(countTo, 15), 15)

    result = multiplesOf3 + multiplesOf5 - multiplesOf15

    print(result)
    return result

solution()