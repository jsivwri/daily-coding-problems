# This problem was asked by Microsoft.

# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

def check(array, string):

    index = 0

    for char in array:
        if char == string[index]:
            index +=1

    return index == len(string)

def word_search(matrix, target):

    for row in matrix:
        if target[0] in row:
            if check(row, target):
                return True
    
    for col_index in range(len(matrix[0])):
        col = [row[col_index] for row in matrix]

        if target[0] in col:
            if check(col, target):
                return True

    return False

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
    ]

assert word_search(matrix, 'FOAM') == True
assert word_search(matrix, 'MASS') == True
assert word_search(matrix, 'WASP') == False