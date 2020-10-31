# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 90

# This question was asked by Google.

# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

import random 

def random_list(n, l):
    int_list = [val for val in range(n) if val not in l]
    if len(int_list) > 0:
        return int_list[random.randint(0,len(int_list)-1)]
    else:
        return None

# TEST CODE:
numbers_0_to_9 = [0 for _ in range(10)]

for _ in range(10000):
    numbers_0_to_9[random_list(10,[2, 3, 5, 7])] += 1

print(numbers_0_to_9)