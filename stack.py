class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    # Assignment 
    def append(self, value):
        self.s.append(value)
    
    # def push(self, value):
    #     self.s.insert(0, value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("The Stack is empty")
        else:
            return self.s[-1]
    
    # def pop(self):
    #     if len(self.s) == 0:
    #         raise Exception("Stack is empty")
    #     else:
    #         return self.s.pop(0)

    # Assignment
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        return self.s.pop()
    

stk = stack()
stk.append(10)
stk.append(20)
stk.append(30)
stk.append(40)
# stk.pop()
print(stk.peek())