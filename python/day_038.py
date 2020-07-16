# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 38

# This problem was asked by Microsoft.

# You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

def queen_arrangements(n, x= -1, y= 0, x_axis = None, y_axis = None, pos_diags = None, neg_diags = None, q = None):
    
    count = 0 

    if x_axis == None:
        x_axis = [0 for _ in range(n)]
        y_axis = [0 for _ in range(n)]
        pos_diags = [0 for _ in range(2*n)]
        neg_diags = [0 for _ in range(2*n)]
        q = n

    if x+1 < n:
        x = x+1
   

    elif y+1 < n:
        y = y+1
        x = 0
    
    else:
        return count
  
    count+= queen_arrangements(n, x, y, x_axis, y_axis, pos_diags, neg_diags, q)

    if x_axis[x] == 0 and y_axis[y] == 0:
        if pos_diags[x+y] == 0 and neg_diags[2+x-y] == 0:
            new_x_axis = x_axis[:]
            new_x_axis[x] = 1

            new_y_axis = y_axis[:]
            new_y_axis[y] = 1

            new_pos_diags = pos_diags[:]
            new_pos_diags[x+y] = 1

            new_neg_diags = neg_diags[:]
            new_neg_diags[2+x-y] = 1
            q -= 1
            count+= queen_arrangements(n, x, y, new_x_axis, new_y_axis, new_pos_diags, new_neg_diags, q)
            
           
        if q == 0:
            count += 1
            return count
        

    return count

assert queen_arrangements(2) == 0
assert queen_arrangements(4) == 2
assert queen_arrangements(5) == 10
assert queen_arrangements(8) == 92