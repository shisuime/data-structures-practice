from collections import deque


class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    

def reverse(string):
    stack=Stack()

    for char in string:
        stack.push(char)

    rstring=''
    while not stack.isEmpty():
        rstring += stack.pop()

    return rstring    


def isMatch(ch1,ch2):
     match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
     return match_dict[ch1] == ch2


def isBalanced(string):
    stack=Stack()

    for char in string:

        if char == '(' or char == '{' or char == '[':
            stack.push(char)

        if char == ')' or char == '}' or char == ']':   

            if stack.size() == 0:
                return False

            if not isMatch(char,stack.pop()):
                return False
            
    return stack.size() == 0        


if __name__ == '__main__':
    ss=Stack()   

    # print(reverse("We will conquere COVI-19"))       
    # print(isBalanced("({a+b})"))
    # print(isBalanced("))((a+b}{"))
    # print(isBalanced("((a+g))"))
    # print(isBalanced("))"))
    print(isBalanced("[a+b]*(x+2y)*{gg+kk}"))
