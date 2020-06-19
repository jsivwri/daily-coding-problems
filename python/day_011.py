#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 11

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


class Tree:

    def __init__(self, entry=None):

        self.children = {}
        self.word = False

        if entry != None:
            self.add_entry(entry)
            

    def add_entry(self, entry):

        entry=entry.lower()

        # set a flag for 'end of word'
        if len(entry)==0:
            self.word = True 

        # create a dictionary entry if needed
        elif entry[0] not in self.children:
            self.children[entry[0]] = Tree(entry[1:])

        # filter the rest of the word down the tree 
        else:
            self.children[entry[0]].add_entry(entry[1:])


    # get_children will only return complete words (self.word flag must be True)
    def get_children(self, string=None, rest=None):

        output = []

        if string == None:
            string=""
        if rest == None:
            rest=""

        
        # if loop to traverse the tree to the node given by the autocomplete string
        if len(string) > 0:
            char = string[0]
            rest = string[1:]
            output = self.children[char].get_children(rest)

            if self.children[char].word == True:
                # an empty flag is added for the loop below to catch
                output+=[''] 

            output = [char+entry for entry in output]
                
            return output


        # if loop to gather every possible word below the autocomplete node
        if len(string)==0:

            keys = self.children.keys()

            for key in keys:
                
                #recursively travel down the tree
                output+=self.children[key].get_children(rest=rest+key)
 
                if self.children[key].word:
                    output.append(rest+key)

            return output


# TEST CODE
autocomplete = Tree()
autocomplete.add_entry("dog")
autocomplete.add_entry("do")
autocomplete.add_entry("deer")
autocomplete.add_entry("deal")
autocomplete.add_entry("dealing")
autocomplete.add_entry("eel")

print(autocomplete.get_children('de'))