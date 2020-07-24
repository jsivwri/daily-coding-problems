# # JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 46

# This problem was asked by Amazon.

# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

def check_pal(input):
    if input == input[::-1]:
        return True
    else:
        return False

def longest_pal(input):
    if check_pal(input):
        return [input]

    elif len(input) < 2:
        return []

    else:
        output = longest_pal(input[1:]) + longest_pal(input[:-1])
        output.sort(key = len)
        return [output[-1]]
    
assert longest_pal('aabcdcb') == ['bcdcb']
assert longest_pal('bananas') == ['anana']