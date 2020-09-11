# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 76

# This problem was asked by Google.

# You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

# For example, given the following table:

# cba
# daf
# ghi
# This is not ordered because of the a in the center. We can remove the second column to make it ordered:

# ca
# df
# gi
# So your function should return 1, since we only needed to remove 1 column.

# As another example, given the following table:

# abcdef
# Your function should return 0, since the rows are already ordered (there's only one row).

# As another example, given the following table:

# zyx
# wvu
# tsr
# Your function should return 3, since we would need to remove all the columns to order it.

def col_in_vals(col):
    return [ord(chr) for chr in col]
    
def col(matrix, num):
    return [row[num] for row in matrix]

def validate_col(col):
    vals = col_in_vals(col)
    prev = None
    for val in vals:
        if prev == None:
            prev = val
        if prev > val:
            return False
    return True

def count_valid_cols(matrix):
    count = 0
    for index in range(len(matrix)):
        column = col(matrix, index)
        if validate_col(column) == False:
            count += 1
    return count

matrix = [
    'zyx',
    'wvu',
    'tsr']
assert count_valid_cols(matrix) == 3

matrix = [
    'abcdef'
]
assert count_valid_cols(matrix) == 0

matrix = [
    'cba',
    'daf',
    'ghi'
]
assert count_valid_cols(matrix) == 1