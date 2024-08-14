from collections import deque
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
    
    def front(self):
        return self.buffer[-1]
q = Queue()
def binary(max):
    q.enqueue("1")
    for i in range(max):
        front = q.front()
        q.enqueue(front + "0")
        q.enqueue(front + "1")

        print(q.dequeue())
    
binary(10)
            
        
        
        