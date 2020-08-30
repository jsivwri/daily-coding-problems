# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 66

# This problem was asked by Square.

# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

# Write a function to simulate an unbiased coin toss.

import random

def toss_biased():
    toss = random.randint(0,99)

    if toss > 20:
        return 0
    else:
        return 1

def toss_n(n):
    cache = 0

    for _ in range(n):
        toss = toss_biased()
        if toss == 1:
            cache += 1
    
    return cache

def toss_even():
    n = 500
    cache = toss_n(n)
    toss_counter = toss_n(n)

    if toss_counter > cache:
        return 1
    elif toss_counter < cache:
        return 0
    else:
        return toss_even()

cache = [0, 0]
for _ in range(1000):
    cache[toss_even()] += 1
print(cache)