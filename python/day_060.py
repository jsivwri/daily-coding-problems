# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 60

# This problem was asked by Facebook.

# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

def split_multiset(multiset, set_1 = None, set_2 = None):
    
    add_to_1 = False
    add_to_2 = False 

    if set_1 == None:
        set_1 = []
    
    if set_2 == None:
        set_2 = []

    sum_set_1 = sum(set_1)
    sum_set_2 = sum(set_2)

    if len(multiset) > 0:

        value = multiset[0]
        new_multiset = multiset[1:]

        sum_new_multiset = sum(new_multiset)

        if sum_set_1 < sum_set_2 + sum_new_multiset:
            new_set_1 = set_1[:]+[value]
            add_to_1 = split_multiset(new_multiset, new_set_1, set_2)

        if sum_set_2 < sum_set_1 + sum_new_multiset:
            new_set_2 = set_2[:]+[value]
            add_to_2 = split_multiset(new_multiset, set_1, new_set_2)

    else:
        if sum_set_1 == sum_set_2:
            return True
        else:
            return False

   
    if add_to_1 == True or add_to_2 == True:
        return True
    else:
        return False 

assert split_multiset([15, 5, 20, 10, 35, 15, 10]) == True
assert split_multiset([15, 5, 20, 10, 35]) == False