# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 29

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

def encode(input):
    cache = [input[0], 1]
    pointer = 1
    output = ""

    while pointer < len(input):
        if cache[0] == input[pointer]:
            cache[1]+=1

        else:
            output += str(cache[1]) + cache[0]
            cache[0] = input[pointer]
            cache[1] = 1

        pointer += 1
    
    return output + str(cache[1]) + cache[0]

assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"