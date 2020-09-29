# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 86

# This problem was asked by Google.

# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

def validate_parentheses(string):
    left_count = 0
    right_count = 0
    error_count = 0 
    for par in string:
        if par == "(":
            left_count += 1
        
        elif par == ")":
            if left_count < right_count + 1:
                error_count += 1
            else:
                right_count += 1

    return error_count + left_count - right_count

assert validate_parentheses("()())()") == 1
assert validate_parentheses(")(") == 2