# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 35

# This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def rgb_filter(rgb_arr):
    r_count = 0
    g_count = 0
    b_count = 0 
    g_pos = 0
    b_pos = 0
    pointer = 0
    swap_count = r_count + g_count + b_count

    # helper to make swap code simpler
    def swap_helper(pointer, pos, count):
        rgb_arr[pointer], rgb_arr[pos+count] = rgb_arr[pos+count], rgb_arr[pointer]

    # first pass to determine total numbers of r, g and b in string
    for val in rgb_arr:
        if val == "R":
            g_pos += 1
            b_pos +=1

        if val == "G":
            b_pos += 1
    
    # second pass to sort the array
    while pointer != len(rgb_arr):
        val = rgb_arr[pointer]

        if pointer < g_pos:
            if val == "R":
                pointer += 1
                r_count += 1

            if val == "G":
                swap_helper(pointer, g_pos, g_count)
                g_count += 1

            if val == "B":
                swap_helper(pointer, b_pos, b_count)
                b_count += 1

        elif pointer < b_pos:
            if val == "R":
                swap_helper(pointer, 0, r_count)
                r_count += 1
                
            if val == "G":
                pointer += 1
                g_count += 1

            if val == "B":
                swap_helper(pointer, b_pos, b_count)
                b_count += 1

        else:
            if val == "R":
                swap_helper(pointer, 0, r_count)
                r_count += 1
            
            if val == "G":
                swap_helper(pointer, g_pos, g_count)
                g_count += 1

            if val == "B":
                pointer += 1
                b_count += 1
    
    return rgb_arr

assert rgb_filter(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']