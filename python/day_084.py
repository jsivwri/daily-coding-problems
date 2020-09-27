# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 84

# This problem was asked by Amazon.

# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

def count_islands(matrix):

    visited = []
    queue = []
    count = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 1:
                count += 1

                if (y, x) not in visited:
                    queue.append((y,x))
                    while queue != []:
                        current = queue.pop(0)
                        current_y, current_x = current
                        matrix[current_y][current_x] = 0
                        visited.append(current)

                        for new_y in range(current_y-1, current_y+2):
                            for new_x in range(current_x-1, current_x+2):
                                if new_y >= 0 and new_y < len(matrix):
                                    if new_x >= 0 and new_x < len(matrix[0]):
                                        if matrix[new_y][new_x] == 1:
                                            queue.append((new_y, new_x))

    return count

matrix = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]

assert count_islands(matrix) == 4