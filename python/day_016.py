#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 16

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.

class Log:
    def __init__(self, n):
        self.log = [None for _ in range(n)]
        self.id_register = 0
        self.n = n
    
    def record(self, order_id):
        self.log.pop(0)
        self.log += [order_id]
        self.id_register += 1

    def get_last(self, i):
        return self.log[self.n-i]
    
# TEST CODE

order_log = Log(4)

order_log.record("001")
order_log.record("002")
order_log.record("003")
order_log.record("004")
order_log.record("005")

assert order_log.get_last(2) == "004"