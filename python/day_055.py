# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 55

# This problem was asked by Microsoft.

# Implement a URL shortener with the following methods:

# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
# Hint: What if we enter the same URL twice?

class Url_short():
    dictionary = {}

    def shorten(self, url):

        shortened = False
        count = 0
        
        while shortened == False: 
            output = [count][:] * 6
            count += 1

            for index in range(len(url)):
                output[index%6] += ord(url[index])

            output_char = [self.num_to_char(val%63) for val in output]

            output_string = ""

            for char in output_char:
                output_string += str(char)

            shortened = self.add_to_dict(url, output_string)

        return output_string

    def num_to_char(self, num):

        if num < 10:
            return chr(48+num)
        elif num < 36:
            return chr(64+num-10)
        else:
            return chr(96+num-36)

    def add_to_dict(self, url, short):

        if short not in self.dictionary.keys():
            self.dictionary[short] = url
            return True

        elif short in self.dictionary.keys() and self.dictionary[short] == url:
            return True

        return False

    def restore(self, short):

        if short in self.dictionary.keys():
            return self.dictionary[short]
        
        else:
            return None

us = Url_short()
assert us.shorten('http://www.google.com') == "jF6NF7"
assert us.restore('jF6NF7') == ('http://www.google.com')