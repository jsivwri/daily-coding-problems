# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 31

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between "kitten" and "sitting" is three: substitute the "k" for "s", substitute the "e" for "i", and append a "g".

# Given two strings, compute the edit distance between them.

def distance(word, target):
    if len(word) == 0 or len(target) == 0:
        return max(len(word), len(target))

    elif word[0] == target[0]:
        return distance(word[1:], target[1:])

    else:
        count_add = 1 + distance(word[1:], target)
        count_del = 1 + distance(word, target[1:])
        count_sub = 1 + distance(word[1:], target[1:])
        
        return min(count_add, count_del, count_sub)

assert distance('kitten', 'sitting') == 3