# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 64

# This problem was asked by Google.

# A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

# Given N, write a function to return the number of knight's tours on an N by N chessboard.

def knights_tour(N, current_pos=(0,0), visited=None):

    y_val, x_val = current_pos
    if visited == None:
        visited = [current_pos]
    
    count = 0
    next_coords = []

    next_coords_total = [
        (y_val - 2, x_val - 1),
        (y_val - 2, x_val + 1),
        (y_val - 1, x_val - 2),
        (y_val - 1, x_val + 2),
        (y_val + 1, x_val - 2),
        (y_val + 1, x_val + 2),
        (y_val + 2, x_val - 1),
        (y_val + 2, x_val + 1)
    ]

    for next_coord in next_coords_total:
        next_y, next_x = next_coord

        if next_y >= 0 and next_x >= 0:
            if next_y < N and next_x < N:
                if next_coord not in visited:
                    next_coords.append(next_coord)
    
    for coord in next_coords:
        new_visited = visited[:]+[coord]
        count += knights_tour(N, coord, new_visited)

    if len(visited) == N*N:
        return 1
    else:
        return count

total = 0
for y in range(5):
    for x in range(5):
        current_pos = (y,x)
        total += knights_tour(5, current_pos)
print(total)

## Brute force solution, so it's super slow!