# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 61

# This problem was asked by Google.

# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

def pow(x, y):
    if y < 0:
        print("only calculates positive powers")
        return None

    elif y == 0:
        return 1
    
    elif y == 1:
        return x

    elif y % 2 == 0:
        return pow(x*x, y//2)

    else:
        return x * pow(x*x, ((y-1) // 2))

assert pow(2,0) == 1
assert pow(2,2) == 4
assert pow(2,3) == 8
assert pow(2,7) == 128