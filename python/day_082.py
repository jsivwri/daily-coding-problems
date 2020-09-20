# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 82

# This problem was asked Microsoft.

# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

# For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".

class File():
    def __init__(self):
        self.pointer = 0 
        self.file_text = "Hello World. The quick brown fox jumps over the lazy dog"

    def return_next_seven(self):
        self.pointer += 7
        return self.file_text[self.pointer-7:self.pointer]

    def reset(self):
        self.pointer = 0

file_read = File()

def read7():
    return file_read.return_next_seven()

def readN(n):
    cache = ""
    pointer = n
    
    while pointer > 0:
        cache += read7()
        pointer -= 7

    file_read.reset()

    return cache[:n]

assert readN(7) == "Hello W"
assert readN(5) == "Hello"
assert readN(10) == "Hello Worl"
assert readN(200) == "Hello World. The quick brown fox jumps over the lazy dog"