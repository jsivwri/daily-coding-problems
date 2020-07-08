# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 30

# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

def fill(container):

    pointer = 1
    first_bound = container[0]
    count = 0
    cache = []

    while pointer < len(container):
        current_num = container[pointer]

        if current_num >= first_bound:
            for num in cache:
                count += first_bound - num

            return count + fill(container[pointer:])

        cache.append(current_num)
        pointer += 1

    if len(container) > 1:
        return count + fill(container[::-1])

    else:
        return count

assert fill([2, 1, 2]) == 1
assert fill([3, 0, 1, 3, 0, 5]) == 8