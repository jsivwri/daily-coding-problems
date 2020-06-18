#JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 10

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


# Job scheduler implementation: 
from multiprocessing import Process
import time

class Job_scheduler:

    def __init__(self):
        self.queue = []
    
    def schedule_job(self, f, n):

        def func():
            time.sleep(n/1000)
            f()

        process = Process(target = func)
        self.queue.append(process)


    def start_queue(self):
        for job in self.queue:
            job.start()


# TEST CODE
# 3 functions, 2 executing simulatenously after 2000ms, and 1 executing 1000ms later

def f1():
    print(time.time())
    print("Job 1")

n1 = 2000


def f2():
    print(time.time())
    print("Job 2")

n2 = 2000


def f3():
    print(time.time())
    print("Job 3")

n3 = 3000

job_scheduler = Job_scheduler()

job_scheduler.schedule_job(f1,n1)
job_scheduler.schedule_job(f2,n2)
job_scheduler.schedule_job(f3,n3)

job_scheduler.start_queue()