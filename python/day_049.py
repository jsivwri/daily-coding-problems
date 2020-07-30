# # JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 49

# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.

def cont_sum(array):
    
    prev_max = 0 
    current = 0

    for val in array:

        if val > 0:
            current += val
        
        else:
            if current + val > 0:
                current += val

            else:
                if prev_max < current:
                    prev_max = current

                current = 0
               
    return max(current, prev_max)

assert cont_sum([34, -50, 42, 14, -5, 86]) == 137
assert cont_sum([-5, -1, -8, -9]) == 0