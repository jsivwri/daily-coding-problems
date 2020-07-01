# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 23

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

class Path_in_matrix():
    def __init__(self, matrix, start, end):
        self.total_y = len(matrix[0])-1
        self.total_x = len(matrix)-1
        self.map = {}
        self.queue = [(start, [])]
        self.target = end
        self.visited = []
        self.h_map = {}

        #define map
        for y in range(self.total_y+1):
            for x in range(self.total_x+1):
                self.map[(x,y)] = matrix[x][y] #I switched these to be in an (x,y) format
        

    def find_path(self):

        current_node, path = self.queue.pop(0)
        self.visited.append(current_node)
        
        path+=[current_node]
        
        if current_node == self.target:
            return len(path)-1

        current_x, current_y = current_node

        adjacent_nodes = []

        if current_x > 0:
            adjacent_nodes.append((current_x - 1, current_y))
        
        if current_y > 0:
            adjacent_nodes.append((current_x, current_y - 1))
        
        if current_x < self.total_x:
            adjacent_nodes.append((current_x + 1, current_y))
        
        if current_y < self.total_y:
            adjacent_nodes.append((current_x, current_y + 1))


        for index in reversed(range(len(adjacent_nodes))):
            if adjacent_nodes[index] in self.visited:
                adjacent_nodes.pop(index)
            elif self.map[adjacent_nodes[index]] == True:
                adjacent_nodes.pop(index)

        for node in adjacent_nodes:
            queue_path = path[:]
            self.queue.append((node, queue_path))


        if len(self.queue) == 0:
            return None       

        return self.find_path()

f = False
t = True 

matrix = [
    [f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]
    ]
map = Path_in_matrix(matrix, (3,0), (0,0))
assert map.find_path() == 7


matrix = [
    [f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, t]
    ]
map = Path_in_matrix(matrix, (0,0), (3,3))
assert map.find_path() == None


matrix = [
    [f, f, f, f, f, f, f, f],
    [t, t, f, t, t, t, t, f],
    [f, f, t, f, f, t, t, f],
    [f, f, f, f, f, t, t, f],
    [f, f, f, f, f, f, f, f]
    ]
map = Path_in_matrix(matrix, (0,0), (3,3))
assert map.find_path() == 16