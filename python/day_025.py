# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 25

# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

def regex_matching(regex, string):

    if len(regex) == 0 and len(string) == 0:
        return True

    if len(regex) == 0 or len(string) == 0:
        return False

    if regex[0] == "." or regex[0] == string[0]:

        if len(regex) > 1 and regex[1] == "*":
            return regex_matching(regex[2:], string[1:]) or regex_matching(regex, string[1:])

        else:
            return regex_matching(regex[1:], string[1:])

    return False

#TEST CODE
assert regex_matching("ra.", "ray")
assert not regex_matching("ra.", "raymond")
assert regex_matching(".*at", "chat")
assert not regex_matching(".*at", "chats")
assert regex_matching(".*f.*","tttttttftttt")
assert regex_matching("a*b*c*","abbccc")