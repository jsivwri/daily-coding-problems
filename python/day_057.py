# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 57

# This problem was asked by Amazon.

# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

def split(string, k):

    words = string.split(" ")
    output = []
    buffer = ""

    for word in words:

        if len(word) > k:
            return None
        elif len(buffer) + 1 + len(word) > k:
            output.append(buffer)
            buffer = ""

        if buffer == "":
            buffer = word
        else:
            buffer = buffer + " " + word

    output.append(buffer)

    return output
        
assert split("the quick brown fox jumps over the lazy dog", 10) == ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog']