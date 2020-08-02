# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 51

# This problem was asked by Facebook.

# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

import random

def return_random(k):
    return random.randint(1, k)

def shuffle():
    non_col_cards = ['A']
    non_col_cards += [str(val+2) for val in range(9)]
    non_col_cards += ['J', 'Q', 'K']
    unshuffled_cards = []
    shuffled_cards = []

    for suit in ['C', 'S', 'H', 'D']:
        unshuffled_cards += [suit+card for card in non_col_cards]

    card = unshuffled_cards.pop(0)
    shuffled_cards = [card]
    
    while len(unshuffled_cards) > 0:
        card = unshuffled_cards.pop(0)
        index = return_random(1 + len(shuffled_cards)) - 1

        shuffled_cards = shuffled_cards[:index] + [card] + shuffled_cards[index:]

    return shuffled_cards

deck = shuffle()

print(deck)
