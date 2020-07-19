# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 39

# This problem was asked by Dropbox.

# Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

map = []
x_max = 0
y_max = 0

def print_map():
    global x_max
    global y_max
    global map
    string = ""
    for x_val in range(x_max+1):
        string += "\n"
        
        for y_val in range(y_max+1):
            if (x_val, y_val) not in map:
                string += "."
            else:
                string += "*"

    print(string)
    

def add_living_cell(x,y):
    
    global x_max
    global y_max
    if x > x_max:
        x_max = x
    
    if y > y_max:
        y_max = y

    if (x,y) not in map:
        map.append((x,y))

def return_neighbours(x, y):
    neighbours = []
    if x > 0 and y > 0:
        neighbours.append((x-1, y-1))
    if x > 0:
        neighbours.append((x-1, y))
        neighbours.append((x-1, y+1))
    if y > 0:
        neighbours.append((x, y-1))
        neighbours.append((x+1, y-1))
    neighbours.append((x, y+1))
    neighbours.append((x+1, y))
    neighbours.append((x+1, y+1))
    
    return neighbours

def step():
    global x_max
    global y_max
    global map
    new_map = []
    live_neighbours = map[:]
    dead_neighbours = []

    for cell in live_neighbours:
        x, y = cell

        if x >= x_max:
            x_max = x + 1
        if y >= y_max:
            y_max = y + 1


    for x_val in range(x_max+1):
        for y_val in range(y_max+1):
            if (x_val, y_val) not in live_neighbours:
                dead_neighbours.append((x_val, y_val))
   
    for cell in live_neighbours:
        count = 0
        x, y = cell

        neighbours = return_neighbours(x,y)
        for neighbour in neighbours:
            if neighbour in live_neighbours:
                count += 1
        if count == 2 or count == 3:
            new_map.append(cell)

    for cell in dead_neighbours:
        count = 0
        x, y = cell
        neighbours = return_neighbours(x,y)
        for neighbour in neighbours:
            if neighbour in live_neighbours:
                count += 1
        if count  == 3: 
            new_map.append(cell)
    map = new_map[:]

def run_game(steps):
    print_map()
    for _ in range(steps):  
        step() 
        print_map()   



add_living_cell(1,1)
add_living_cell(0,1)
add_living_cell(1,0)
add_living_cell(2,2)
add_living_cell(2,1)
add_living_cell(1,2)
add_living_cell(3,0)
add_living_cell(3,3)
add_living_cell(4,4)
run_game(15)




