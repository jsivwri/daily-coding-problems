# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 54

# This problem was asked by Dropbox.

# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

# Implement an efficient sudoku solver.

def increment(x, y):
    x += 1

    if x > 8:
        x = 0
        y += 1

    return x, y

def decrement(x, y):
    x -= 1

    if x < 0:
        x = 8
        y -= 1

    return x, y

def return_row(grid, row):
    return grid[row]

def return_col(grid, col):
    return [row[col] for row in grid]

def return_nonet(grid, row, col):
    row_num = 3 * (row // 3)
    col_num = 3 * (col // 3)
    nonet = []

    for y in range(row_num, row_num + 3):
        for x in range(col_num, col_num + 3):
            nonet.append(grid[y][x])
    return nonet

def check_valid_array(array):
    hits = [0 for _ in range(10)]
    for val in array:
        if val > 0:
            if hits[val] == 1:
                return False
            hits[val] = 1
    return True 



def solve(board):

    board_copy = []
    for line in start_board:
        board_copy += [line[:]]

    y_index = 0 
    x_index = 0 

    while y_index != 9:

        if board[y_index][x_index] == 0:
            board_copy[y_index][x_index] += 1

            if board_copy[y_index][x_index] == 10:
                board_copy[y_index][x_index] = 0
                x_index, y_index = decrement(x_index, y_index)

                while board[y_index][x_index] != 0:
                    x_index, y_index = decrement(x_index, y_index)

            else:
        
                row = return_row(board_copy, y_index)
                col = return_col(board_copy, x_index)

                if check_valid_array(row) and check_valid_array(col):
                    x_index, y_index  = increment(x_index, y_index)

        else:
            x_index, y_index  = increment(x_index, y_index)

    return board_copy


start_board = [
[0,0,4,0,8,0,6,9,7],
[0,0,0,2,0,0,4,0,0],
[5,9,6,1,0,4,0,0,8],
[0,0,9,6,1,0,0,7,0],
[8,3,0,7,0,9,0,6,5],
[0,7,0,0,5,2,9,0,0],
[3,0,0,9,0,1,5,8,6],
[0,0,8,0,0,7,0,0,0],
[9,2,5,0,6,0,7,0,0]
]

print(solve(start_board))