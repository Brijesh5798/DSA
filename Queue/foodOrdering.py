from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
q = Queue()  
def placeOrder(arr):
    for i in arr:
        q.enqueue(i)
        time.sleep(0.5)

def serveOrder():
    while q.is_empty() == False:
        print(q.dequeue())
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(placeOrder(orders))
t2 = threading.Thread(serveOrder())

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()