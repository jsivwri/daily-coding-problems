#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 15

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.

class Log:
    def __init__(self):
        self.log = []
        self.id_register = 0
    
    def record(self, order_id):
        self.log += [order_id]
        self.id_register += 1

    def get_last(self, i):
        if i < 1:
            return "i must be greater than 0"
        return self.log[self.id_register-i]
    
# TEST CODE

order_log = Log()

order_log.record("001")
order_log.record("002")
order_log.record("003")

assert order_log.get_last(2) == "002"
