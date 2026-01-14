from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,data):
        self.container.appendleft(data)   

    def pop(self):
        return self.container.popleft()  

    def peek(self,val):
        return self.container[-val]

    def size(self):
        return len(self.container)  

    def isEmpty(self):
        return len(self.container)== 0    
    
    def __str__(self):
        return str(list(self.container))


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())