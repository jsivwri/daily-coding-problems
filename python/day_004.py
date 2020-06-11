#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 4

#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.

def find_lmv( array, num=1 ): 

    for val in array:
        if val == num:
            num = find_lmv(array, num+1)

    return num

# TESTS
assert find_lmv([3, 4, -1, 1]) == 2
assert find_lmv([1,2,0]) == 3
assert find_lmv([1]) == 2
assert find_lmv([0]) == 1
assert find_lmv([-1,-1,-1]) == 1
assert find_lmv([0,0,0]) == 1
assert find_lmv([9,8,6,5,4,3,2]) == 1
assert find_lmv([9,8,1,6,5,4,3,2,1,-1,0,0,-10]) == 7
assert find_lmv([-10,-14,0,0,1,3]) == 2