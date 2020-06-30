#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 22

# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

class Dictionary():
    def __init__(self, word_list):
        self.dictionary = []
        for word in word_list:
            self.dictionary+=[word]

    def parse(self, word_string, current_string=None, current_words = None, complete=False):
        if current_string == None:
            current_string = ""
        if current_words == None:
            current_words = []
        first_letter = word_string[0]
        word_string = word_string[1:]

        if current_string + first_letter in self.dictionary:
            current_words += [current_string + first_letter]
            
            current_string = ""
        
        else:
            current_string += first_letter
        
        if len(word_string) > 0:
            current_words, complete = self.parse(word_string, current_string, current_words)

        else:
            if len(current_string) == 0:
                complete = True 

        if complete == False:
            word_string = current_string
            try:
                current_string = current_words.pop(-1)
                current_words, complete = self.parse(word_string, current_string, current_words)

            except:
                complete = True
                current_words = "Parse not possible"
                
        
        return current_words, complete

    def parser(self, word_string):
        current_words, _ = self.parse(word_string)
        return current_words

# TEST CODE

dictionary = Dictionary(['quick', 'brown', 'the', 'fox'])
assert dictionary.parser("thequickbrownfox") == ['the', 'quick', 'brown', 'fox']

dictionary2 = Dictionary(['quick', 'brown', 'the', 'fox', 'quicking'])
assert dictionary2.parser("thequickingbrownfox") == ['the', 'quicking', 'brown', 'fox']

dictionary3 = Dictionary(['bed', 'bath', 'bedbath', 'and', 'beyond']) 
assert dictionary3.parser("bedbathandbeyond") == ['bed', 'bath', 'and', 'beyond']

dictionary4 = Dictionary(['bed', 'bath', 'bedbath', 'beyond']) 
assert dictionary4.parser("bedbathandbeyond") == 'Parse not possible'     