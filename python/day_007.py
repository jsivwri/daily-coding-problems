#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 7

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode(msg):

    total = 0

    if len(msg) > 1:
        if int(msg[:2]) <= 26 and int(msg[0]) != 0:
            total += decode(msg[2:])

        if int(msg[0]) != 0:
            total += decode(msg[1:])

    if (len(msg)==1 and int(msg[0]) != 0) or len(msg)==0:
        total+=1
    
    return total 
 

#TESTS

assert decode('111')==3
assert decode('1111')==5
assert decode('11111')==8
assert decode('262626')==8
assert decode('272727')==1
assert decode('01212')==0




