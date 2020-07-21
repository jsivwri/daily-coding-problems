# # JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 44

# This problem was asked by Google.

# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

def count_inversions(array):
    pointer = 0
    counter = 0

    while pointer < len(array):
        if pointer > 0:
            p = pointer
            while p != 0 and array[p] < array[p-1]:
                array[p], array[p-1] = array[p-1], array[p]
                p -= 1
                counter += 1
        pointer += 1

    return counter

count_inversions([2, 4, 1, 3, 5]) == 3
count_inversions([5,4,3,2,1]) == 10