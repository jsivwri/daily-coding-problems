# # JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 45

# This problem was asked by Two Sigma.

# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

import random 

def rand5():
    return random.randint(1,5)

def rand7():
    cache = 0
    for _ in range(7):
        cache += rand5()
    return cache % 7

# CODE DEMO
totals = [0] * 7 
for _ in range(100000):
    num = rand7()
    totals[num-1] += 1

print(totals)