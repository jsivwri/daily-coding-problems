# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 53

# This problem was asked by Apple.

# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack = [data] + self.stack

    def pop(self):
        return self.stack.pop(0)

class Queue:
    def __init__(self):
        self.standard_stack = Stack()
        self.reversed_stack = Stack()
        self.dequeue_ready = False

    def enqueue(self, data):
        if self.dequeue_ready == True:
            self.reverse_stacks(self.reversed_stack, self.standard_stack)
            self.dequeue_ready = False

        self.standard_stack.push(data)

    def dequeue(self):
        if self.dequeue_ready == False:
            self.reverse_stacks(self.standard_stack, self.reversed_stack)
            self.dequeue_ready = True

        return self.reversed_stack.pop()
        
    def reverse_stacks(self, source, target):
        while True:
            try:
                target.push(source.pop())
            except IndexError:
                return

stack_queue = Queue()

stack_queue.enqueue(1)
stack_queue.enqueue(2)
assert stack_queue.dequeue() == 1
stack_queue.enqueue(3)
stack_queue.enqueue(4)
assert stack_queue.dequeue() == 2
assert stack_queue.dequeue() == 3
stack_queue.enqueue(5)
assert stack_queue.dequeue() == 4
assert stack_queue.dequeue() == 5