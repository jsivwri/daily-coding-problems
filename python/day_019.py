#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 19

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

def min_cost(matrix, current_house = None, current_total = None, previous_color = None):
    
    if current_house == None:

        current_house = 0

        for color in range(len(matrix[0])):
            current_total = matrix[0][color]
            previous_color = color
            min_cost(matrix, current_house, current_total, previous_color)
    
    else:

        current_house += 1

        if current_house == len(matrix):
            global global_min

            if global_min == None:
                global_min = current_total

            else:
                if current_total < global_min:
                    global_min = current_total

            return

        for color in range(len(matrix[current_house])):
            if color == previous_color:
                pass

            else:
                previous_color = color
                min_cost(matrix, current_house, current_total+matrix[current_house][color], previous_color)

    return global_min

# TEST CODE

matrix = [
    [1, 2, 1, 2],     #row n0
    [1, 2, 3, 4],     #row n1
    [5, 6, 5, 6],     #row n2
    [10, 10, 0, 10]   #row n3
]
global_min = None

assert min_cost(matrix) == 7