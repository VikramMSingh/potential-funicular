from collections import deque 

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        self.container.pop()

    def peek(self):
        self.container[-1]
    
    def is_empty(self):
        return len(self.container == 0)
    
    def size(self):
        return len(self.container)

if __name__ == '__main__':
    stack = Stack()