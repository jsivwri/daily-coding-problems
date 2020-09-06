# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 71

# This problem was asked by Two Sigma.

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

import random 

def rand7():
    return random.randint(1,7)

def rand5():
    roll = rand7()

    if roll >= 6:
        return rand5()

    return roll

# CODE DEMO
totals = [0 for _ in range(5)] 
for _ in range(100000):
    num = rand5()
    totals[num-1] += 1

print(totals)