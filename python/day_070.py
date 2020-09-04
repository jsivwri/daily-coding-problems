# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 70

# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

def sum_digits(n):
    if n > 9:
        return sum_digits (n // 10) + n % 10
    
    else:
        return n % 10

def nth_number(n):
    sum = sum_digits(n)

    if sum > 10:
        return None

    elif sum == 10:
        return n

    else:
        new_dig = 10 - sum
        if n % 10 == 0:
            n = n + new_dig
        else:
            n = n*10 + new_dig
        return n

assert nth_number(2) == 28
assert nth_number(29) == None
assert nth_number(105) == 1054
assert nth_number(150) == 154