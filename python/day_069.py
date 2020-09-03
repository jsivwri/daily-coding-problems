# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 69

# This problem was asked by Facebook.

# Given a list of integers, return the largest product that can be made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

# You can assume the list has at least three integers.

class integer_cache:
    def __init__(self, n, modifier = None):
        self.cache = [None for _ in range(n)]
        self.modifier = modifier

    def add(self, val):
        if None in self.cache:
            self.cache = [abs(val)]+self.cache[:-1]
        else:
            self.cache.sort()
            if self.modifier == min and abs(val) < self.cache[-1]:
                self.cache = self.cache[:-1] + [abs(val)]
            elif abs(val) > self.cache[0]:
                self.cache = [abs(val)] + self.cache[1:]

    def return_vals(self):
        return [val for val in self.cache if val != None]


def largest_product(lst):

    if len(lst) == 3:
        return lst[0] * lst[1] * lst[2]

    pos_cache = integer_cache(3)
    neg_cache = integer_cache(2)
    min_cache = integer_cache(3, min)

    for val in lst:
        if val > 0:
            pos_cache.add(val)
            min_cache.add(val)
        
        elif val < 0:
            neg_cache.add(val)
            min_cache.add(val)
    
    neg_vals = neg_cache.return_vals()
    pos_vals = pos_cache.return_vals()
    min_vals = min_cache.return_vals()

    if len(pos_vals) == 0 or (len(pos_vals) == 2 and len(neg_vals) == 1):
        return min_vals[0] * min_vals[1] * min_vals[2]

    elif len(neg_vals) == 2:
        if len(pos_vals) >= 2:
            if neg_vals[0]*neg_vals[1] > pos_vals[0]*pos_vals[1]:
                return neg_vals[0]*neg_vals[1]*max(pos_vals)
        else:
            return neg_vals[0] * neg_vals[1] * pos_vals[0]
    
    else:
        return pos_vals[0] * pos_vals[1] * pos_vals[2]

assert largest_product([-10, -10, 5, 2]) == 500
assert largest_product([-10, -10, -1, -2]) == 20
assert largest_product([10, -2, -2]) == 40