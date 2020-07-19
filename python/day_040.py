# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 40

# This problem was asked by Google.

# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.

def find_non_trip(array):
    cache = [0] * 16
    output = ""

    for val in array:
        for x in range(len(bin(val)[2:])):
            cache[-1-x] += int(bin(val)[-1-x])

    for index in range(len(cache)):
        output += str(cache[index] % 3)
         
    return int(output, 2)


assert find_non_trip([6, 1, 3, 3, 3, 6, 6]) == 1
assert find_non_trip([13, 19, 13, 13]) == 19