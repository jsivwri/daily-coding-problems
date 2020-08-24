# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 62

# This problem was asked by Facebook.

# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

def path(N, M):

    if N == 0 or M == 0:
        return 0 

    if N == 1 and M == 1:
        return 1

    return path(N-1, M) + path(N, M-1)

assert path(2,2) == 2
assert path(5,5) == 70