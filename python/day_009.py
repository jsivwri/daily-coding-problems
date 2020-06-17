#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 9

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(int_arr):

    if len(int_arr) == 0:
        return 0
    
    if int_arr[0] < 0:
        int_arr[0] = 0

    out_a = int_arr[0] + largest_sum(int_arr[2:])


    if len(int_arr) == 1:
        return out_a

    if int_arr[1] < 0:
        int_arr[1] = 0

    out_b = int_arr[1] + largest_sum(int_arr[3:])

    if out_a >= out_b:
        return out_a
    else:
        return out_b

print(largest_sum([3,3,4,5,2,1]))

