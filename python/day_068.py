# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 68

# This problem was asked by Google.

# On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

# You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

# For example, given M = 5 and the list of bishops:
# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)

# The board would look like this:

# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

def bishop_attack(m, tuples):
    pos_count = [0 for _ in range(2*m)]
    neg_count = [0 for _ in range(2*m)]
    attack_count_cache = {}
    attack_count_cache[0] = 0
    attack_count_cache[1] = 0
    attack_count_cache[2] = 1
    attack_count = 0

    for bishop in tuples:
        x, y = bishop
        pos_diag = x + y
        neg_diag = x - y
        pos_count[pos_diag] += 1
        neg_count[neg_diag + m] += 1

    for count in pos_count:
        pointer = 0
        while count not in attack_count_cache.keys():
            if pointer not in attack_count_cache.keys():
                attack_count_cache[pointer]=attack_count_cache[pointer-1]+pointer
            pointer += 1
        attack_count += attack_count_cache[count]
    
    for count in neg_count:
        pointer = 0
        while count not in attack_count_cache.keys():
            if pointer not in attack_count_cache.keys():
                attack_count_cache[pointer]=attack_count_cache[pointer-1]+pointer
            pointer += 1
        attack_count += attack_count_cache[count]

    return attack_count        

tuples = [(0, 0), (1, 2), (2, 2), (4, 0)]
m = 5
assert bishop_attack(m, tuples) == 2

tuples = [(0, 0), (1, 2), (2, 2), (4, 0), (3,0), (2,1), (1,2), (0,3)]
m = 5
assert bishop_attack(m, tuples) == 16