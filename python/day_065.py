# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 65

# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

def return_top(matrix):
    top = matrix[0]
    matrix = matrix[1:]
    return top, matrix

def return_bottom(matrix):
    bottom = matrix[-1][::-1]
    matrix = matrix[:-1]
    return bottom, matrix

def return_right(matrix):
    right = [line[-1] for line in matrix]
    matrix = [line[:-1] for line in matrix]
    return right, matrix

def return_left(matrix):
    left = [line[0] for line in matrix][::-1]
    matrix = [line[1:] for line in matrix]
    return left, matrix

def print_line(line):
    for val in line:
        print(val)

def spiral_print(matrix):
    count = 0

    while len(matrix) > 0:
        if count % 4 == 0:
            line, matrix = return_top(matrix)

        if count % 4 == 1:
            line, matrix = return_right(matrix)

        if count % 4 == 2:
            line, matrix = return_bottom(matrix)

        if count % 4 == 3:
            line, matrix = return_left(matrix)

        count += 1 

        print_line(line)

matrix = [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]

spiral_print(matrix)