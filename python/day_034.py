# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 33
 
# This problem was asked by Quora.

# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

## Find the smallest pivot:
### start in the middle, look outwards
### move left and right 1 and look outwards from each
#### if partial palindrome found, complete it
## stop at end 

def check_palindrome(word):
    if word == word[::-1]:
        return True
    return False 


def complete_pal(word):

    if check_palindrome(word):
        return word

    if word[0]==word[-1]:
        return word[0] + complete_pal(word[1:-1]) + word[-1]
    
    else:
        option_one = complete_pal(word[-1] + word)
        option_two = complete_pal(word + word[0])
    
    if len(option_one) > len(option_two):
        return option_two
    
    elif len(option_one) < len(option_two):
        return option_one
    
    elif ord(option_one[0]) < ord(option_two[0]):
        return option_one

    else:
        return option_two

assert complete_pal("google") == "elgoogle"
assert complete_pal("race") == "ecarace"