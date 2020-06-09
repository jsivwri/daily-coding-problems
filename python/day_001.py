#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 1

def sum_to_k(k,lst):
    # if a number in 'list' can sum to 'k', it will be found in this array during iteration
    possible_pairs = []

    for num in lst:
        if num in possible_pairs:
            return True
        possible_pairs.append(k-num)
    return False

# STANDARD TESTS
print(sum_to_k(17,[10,15,3,7]))

# LOOK FOR CORNER CASES
print(sum_to_k(20,[10,10]))
print(sum_to_k(0,[10,15,0,1]))
print(sum_to_k(10,[0,-5,15,3]))