#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 15

# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random 
import math

# Exploits 1/n = 1/2 * 2/3 ... * n-3/n-2 * n-2/n-1 to make a random selection based on the current data count. 
# Lots of random numbers needed!
class find_random_data_point:
    def __init__(self):
        self.counter = 0
        self.random_data = None

    def reset(self):
        self.counter = 0

    def begin_stream(self, data):
        self.counter += 1
        if random.randrange(self.counter) == 0:
            self.random_data = data

    def return_random_data(self):
        return self.random_data


# TEST CODE
randomiser = find_random_data_point()

data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

distribution = [0 for _ in data]

for _ in range(160000):
    randomiser.reset()
    for d in data:
        randomiser.begin_stream(d)
    distribution[randomiser.random_data]+=1

print(distribution) # an 'equal' distribtion would yeild 10,000 per point in the list
