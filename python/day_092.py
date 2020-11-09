# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 92

# This problem was asked by Airbnb.

# We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

# Return null if there is no such ordering.

# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSC300'].

class Node:
    def __init__(self, name):
        self.name = name
        self.prerequisites = []

class Database:
    def __init__(self):
        self.head = None
        self.head_count = 0
        self.dict = {}

    def add_data(self, data):
        for key in data.keys():
            if key not in self.dict.keys():
                self.dict[key] = Node(key)
                self.dict[key].prerequisites = data[key]
                if len(self.dict[key].prerequisites) > self.head_count:
                    self.head = key
                    self.head_count = len(self.dict[key].prerequisites)

    def return_sorted_order(self):
        current_list = [self.head]
        sorted_order = []
        
    
        while len(current_list) > 0:
            new_current_list = []
            old_current_list = current_list[:]

            for code in current_list:
                new_codes = self.dict[code].prerequisites
                for new_code in new_codes:
                    if new_code not in new_current_list:
                        new_current_list.append(new_code)
                    while new_code in old_current_list:
                        old_current_list.remove(new_code)
            
            current_list = new_current_list
            if len(old_current_list) == 0:
                return None

            sorted_order = old_current_list + sorted_order

        return sorted_order

courses = {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
    }
data = Database()
data.add_data(courses)

assert data.return_sorted_order() == ['CSC100', 'CSC200', 'CSC300']