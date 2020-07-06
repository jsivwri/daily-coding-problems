# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 28

# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

def length_of_list(list):
    output = ""
    for word in list:
        output += word

    return len(output)


def pad(line, k):
    length = len(line)
    count = k - length_of_list(line)
    index = 0
    while count > 0:
        if line[index%length].isspace():
            line[index%length]+=" "
            count -= 1

        index += 1

    return line


def list_to_string(line):
    output = ""
    for word in line:
        output += word

    return output


def text_justify(word_list, k):
    output = []

    while len(word_list) > 0:
        line = []
        while length_of_list(line) != k and len(word_list) > 0:
            if 16 - length_of_list(line) >= len(word_list[0]):
                line += [word_list.pop(0)]
                if 16 - length_of_list(line) > 2 and len(word_list) != 0:
                    line += [" "]

                if 16 - length_of_list(line) == 1: 
                    line = [line.pop(0)]+[" "]+line

            else:
                line = pad(line, 16)

        if length_of_list(line) != k:
            line = pad(line, 16)     

        line = list_to_string(line)     
        output += [line]

    print(output)


# TEST CODE
list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
text_justify(list, 16)