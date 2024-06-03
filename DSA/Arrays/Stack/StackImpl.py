# Implementing a stack is trivial using a dynamic array
# (which we implemented earlier).
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

    def printStack(self):
        print(self.stack)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.printStack()
print(f"value popped from stack is : {s.pop()}")
s.printStack()