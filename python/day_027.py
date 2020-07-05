# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 27

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

def bracket_parser(string):

    queue = []

    while len(string)>0:
        char = string[0]
        string = string[1:]

        if char == '[':
            queue.append(']')

        elif char == '(':
            queue.append(')')

        elif char == '{':
            queue.append('}')

        elif char == ']' or char == ')' or char == '}':
            if queue.pop(-1) != char:
                return False
    
    if len(queue) == 0:
        return True

    return False

# TEST CODE
assert bracket_parser("([])") == True
assert bracket_parser("([)]") == False
assert bracket_parser("((()") == False
assert bracket_parser("(a+b)*{(ab)/[ab]}") == True