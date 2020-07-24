# # JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 47

# This problem was asked by Facebook.

# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

def stock_profit(array):
    assert len(array) > 1
    min_val = array[0]
    best_profit = 0
    pointer = 1

    while pointer < len(array):

        if array[pointer] - min_val > best_profit:
            best_profit = array[pointer] - min_val

        if min_val > array[pointer]:
            min_val = array[pointer]

        pointer += 1

    return best_profit

assert stock_profit([9, 11, 8, 5, 7, 10])