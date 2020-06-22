#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 14

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

def estimate_pi(num_of_tests):
    count = 0
    loop_count = 0
    while loop_count < num_of_tests:  
        loop_count+=1  
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            count += 1
        pi = 4.0*count/loop_count
    
    return pi
    

assert(round(estimate_pi(10000000), 3)) == 3.141