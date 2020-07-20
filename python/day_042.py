# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 42

# This problem was asked by Google.

# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

def subset_sum_to_k(S, k):

    if k == 0:
        return []
    
    for index in range(len(S)):
        solution = subset_sum_to_k(S[index+1:], k-S[index])
        if solution != None:
            return [S[index]] + solution
            
    return None

assert subset_sum_to_k([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]