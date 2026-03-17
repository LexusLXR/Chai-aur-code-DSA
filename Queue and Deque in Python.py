
# <---------------------------------------Queue----------------------------------------------------------->

class Queue:
    def __init__(self):
        self.items = []

    def isEmpt(self):
        return len(self.items) == 0
    
    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if(self.isEmpt()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete()


# <-------------------------Deque--------------------------------------------->

class Deque:
    def __init__(self):
        self.items = []

    def isEmpt(self):
        return len(self.items) == 0
    
    def insertAtEnd (self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if(self.isEmpt()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
    def insertAtFront(self, value):
        self.items.insert(0, value) 

    def deletionAtEnd(self):
        if(self.isEmpt()):
            print("Queue is Empty")
        else:
            return self.items.pop()

dq = Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)

print(dq.deletionAtEnd())
print(dq.deletionAtEnd())
print(dq.deleteAtFront())
print(dq.deleteAtFront())
print(dq.deletionAtEnd())
dq.deletionAtEnd()