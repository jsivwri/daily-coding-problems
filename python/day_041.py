# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 41

# This problem was asked by Facebook.

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

def find_path(flights, origin, route = None):
    best_route = None
   
    if route == None:
        route = [origin]
        
    else:
        route = route + [origin]
    
    if len(flights) == 0:
        return route
    
    for index in range(len(flights)):
        start, end = flights[index]
        if origin == start:
            new_flights = flights[:index]+flights[index+1:]
            best_route = find_path(new_flights, end, route)

    return best_route
            
assert find_path([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert find_path([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None
assert find_path([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') == ['A', 'C', 'A', 'B', 'C']