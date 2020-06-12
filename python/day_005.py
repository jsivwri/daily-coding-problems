#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 5

#This problem was asked by Jane Street.

#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f): 
        return f(a, b)
    return pair

# Implement car and cdr.

def car(pair):
    return pair(lambda a, b : a)

def cdr(pair):
    return pair(lambda a, b : b)

# Understanding this problem was the hardest part for me. It took me on a deep-end dive into functional programming.
# If that is a new area for you (like it was for me), I'd recommend this as a starting place: https://inst.eecs.berkeley.edu/~cs61a/sp18/lab/lab02/

# TESTS
assert car(cons(3,2)) == 3
assert cdr(cons(3,2)) == 2