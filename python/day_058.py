# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 58

# This problem was asked by Amazon.

# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.

def find(array, val):

    lower = array[0]
    upper = array[-1]
    mid = array[(len(array)-1)//2]

    lower_index = 0
    upper_index = len(array) - 1
    mid_index = (len(array)-1)//2

    lower = array[lower_index]
    upper = array[upper_index]
    mid = array[mid_index]

    if lower == val:
        return 0
    
    elif upper == val:
        return len(array)-1

    elif mid == val:
        return (len(array) - 1) // 2

    if len(array) <= 3:
        return None


    if mid < val and (upper > val or upper - mid < 0):
        index = find(array[mid_index:upper_index], val)
        if index == None:
            return None

        return mid_index + index

    elif lower < val or mid - lower < 0:
        index = find(array[0:mid_index], val)
        if index == None:
            return None

        return index

    else:
        index = find(array[mid_index:upper_index], val)
        if index == None:
            return None

        return mid_index + index

assert find([13, 18, 25, 2, 8, 10], 8) == 4