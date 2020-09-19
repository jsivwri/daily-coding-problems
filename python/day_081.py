# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 81

# This problem was asked by Yelp.

# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

# For example if ['2': ['a', 'b', 'c'], 3: ['d', 'e', 'f'], ...] then '23' should return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].

def num_to_charset(num):
    if num <= 1 or num > 9:

        return None

    elif num < 8:
        num = (num-2)*3
        charset = [chr(97+val) for val in range(num,num+3)]
        if num == 15:
            charset.append('s')

    else:
        num = ((num-2)*3)+1
        charset = [chr(97+val) for val in range(num,num+3)]
        if num == 22:
            charset.append('z')

    return charset

def string_to_set(string):
    string=str(string)
    output = None
    for val in string:
        if output == None:
            output = num_to_charset(int(val))
        
        else:
            new_string = num_to_charset(int(val))
            new_output = []
            for chars in output:
                for char in new_string:
                    new_output.append(chars+char)
            output = new_output
    
    return output

assert string_to_set(23) == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']