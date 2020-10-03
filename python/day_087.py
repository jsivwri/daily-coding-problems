# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 87

# This problem was asked by Uber.

# A rule looks like this:

# A NE B

# This means this means point A is located northeast of point B.

# A SW C

# means that point A is southwest of C.

# Given a list of rules, check if the sum of the rules validate. For example:

# A N B
# B NE C
# C N A
# does not validate, since A cannot be both north and south of C.

# A NW B
# A N B
# is considered valid.

class Node:
    def __init__(self, val):
        self.val = val
        self.N = []
        self.S = []
        self.E = []
        self.W = []

class Map:
    def __init__(self):
        self.dict = {}

    def add_rule(self, rule):
        node_a = rule[0]
        node_b = rule[-1]
        locations = rule[1:-1].strip()

        if node_a not in self.dict.keys():
            self.dict[node_a] = Node(node_a)

        if node_b not in self.dict.keys():
            self.dict[node_b] = Node(node_b)

        for location in locations:
            if self.validate_locations(node_a, node_b, location):
                self.add_locations(node_a, node_b, location)
                self.add_locations(node_b, node_a, self.switch_poles(location))

            else:
                return False

            return True

    def add_locations(self, node_a, node_b, pole):
        if pole == "N":
            self.dict[node_a].N.append(node_b)

        elif pole == "S":
            self.dict[node_a].S.append(node_b)

        elif pole == "E":
            self.dict[node_a].E.append(node_b)

        elif pole == "W":
            self.dict[node_a].W.append(node_b)

    def validate_locations(self, node_a, node_b, pole):
        node_b_pole_locations = self.return_locations_at_pole(node_b, pole)

        if node_a in node_b_pole_locations:
            return False
        
        return True

    def return_locations_at_pole(self, node, pole):
        if pole == "N":
            locations = self.dict[node].N

        elif pole == "S":
            locations = self.dict[node].S

        elif pole == "E":
            locations = self.dict[node].E

        elif pole == "W":
            locations = self.dict[node].W

        for location in locations:
            locations.extend(self.return_locations_at_pole(location, pole))

        return locations

    def switch_poles(self, pole):
        if pole == "N":
            return "S"

        elif pole == "S":
            return "N"
        
        elif pole == "E":
            return "W"

        elif pole == "W":
            return "E"

map = Map()
assert map.add_rule('A NW B') == True
assert map.add_rule('A N B') == True

map = Map()
assert map.add_rule('A N B') == True
assert map.add_rule('B NE C') == True
assert map.add_rule('C N A') == False