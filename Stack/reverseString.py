from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def reverse(string):
    stack = Stack()
    for i in string:
        # print(i)
        stack.push(i)
    new_string = ""
    while stack.is_empty() == False:
        new_string = new_string + stack.pop()
    return new_string

def is_match(ch1, ch2):
    paran = {'(':')', '[':']', '{':'}'}
    return paran[ch2] == ch1
    
def is_balanced(str):
    stack = Stack()
    for i in str:
        if i == '(' or i == '[' or i == '{':
            stack.push(i)
        if i == ')' or i == ']' or i == '}':
            if stack.size() == 0:
                return False
            if not is_match(i,stack.pop()):
                return False
    return stack.size() == 0
    
            
if __name__ == '__main__':
    print(reverse("We will conquere COVI-19"))
    print(reverse("I am the king"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))