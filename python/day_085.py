# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 85

# This problem was asked by Facebook.

# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

def mux(x, y, b):
    return y * b + x * (1-b)

x = 1988
y = 1066

assert mux(x, y, 0) == x
assert mux(x, y, 1) == y