#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 21

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

class Scheduler:
    def __init__(self):

        self.first_classroom = None
        self.last_classroom = None

    def add_classes(self, class_list):

        classroom = self.first_classroom

        for class_times in class_list:

            while classroom != None:

                if classroom.check_available(class_times) == True: 
                    break

                classroom = classroom.next_classroom

            if classroom == None:
                classroom = self.new_classroom()

            classroom.add_class(class_times)    

            classroom = self.first_classroom

    def new_classroom(self):
        classroom = Classroom()

        if self.last_classroom != None:
            self.last_classroom.next_classroom = classroom

        self.last_classroom = classroom

        if self.first_classroom == None:
            self.first_classroom = classroom
            
        return classroom

    def count_classrooms(self):

        count = 0 

        classroom = self.first_classroom

        while (classroom != None):
            count += 1
            classroom = classroom.next_classroom

        return count
            

class Classroom:
    def __init__(self):
        self.classes = []
        self.next_classroom = None

    def add_class(self, class_times):
        self.classes.append(class_times)

    def check_available(self, class_times):
        start_time, end_time = class_times
        for scheduled_class in self.classes:
            class_start_time, class_end_time = scheduled_class

            if start_time > class_start_time:
                if start_time < class_end_time:
                    return False
            
            if end_time > class_start_time: 
                if start_time < class_end_time:
                    return False
            
            if end_time < class_start_time:
                break
        
        return True

# TEST CODE

scheduler = Scheduler()
scheduler.add_classes([(30, 75), (0, 50), (60, 150)])
assert scheduler.count_classrooms() == 2

scheduler = Scheduler()
scheduler.add_classes([(30, 75), (30,150), (0, 50), (60, 150), (50,60),(0,30)])
assert scheduler.count_classrooms() == 3