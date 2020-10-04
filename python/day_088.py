# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 88

# This question was asked by ContextLogic.

# Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

def div(int_a, int_b):
    count = 0

    cache = [1, 2]
    sub = [int_b, int_b+int_b]

    while int_a >= int_b:
        if int_a >= sub[1]:
            int_a -= sub[1]
            count += cache[1]

            cache = [cache[1], cache[0] + cache[1]]
            sub = [sub[1], sub[0] + sub[1]]

        else:
            cache = [cache[1] - cache[0], cache[0]]
            sub = [sub[1] - sub[0], sub[0]]

    return count

assert div(100000000000000000000000000000000000,3) == 33333333333333333333333333333333333