# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 79

# This problem was asked by Facebook.

# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

def modify_array(array):
    pointer = 1
    modified = False
    cache = array[0]

    while pointer < len(array):
        if cache > array[pointer]:
            if modified == False:
                modified = True

            else:

                return False
            
        cache = array[pointer]
        pointer += 1
    
    return True 

assert modify_array([10, 5, 7]) == True
assert modify_array([10, 5, 1]) == False
assert modify_array([5, 5, 6, 5]) == True