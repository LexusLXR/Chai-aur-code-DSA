class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        t = self.head
        while(t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next =self.head
        self.head.prev = temp
        self.head = temp 

    def insertAtMid(self,value, x):
        t = self.head

        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    
    def deletionInDLL(self, value):
        if(self.head == None):
            print("Linked List is Empty")
            return
        
        t = self.head
        # deletion in the beginning
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        # deletion in the middle
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        # deletion at the end
        if(t.data == value):
            t.prev.next = None

    #Assignment
    def circularLL(self):
        if self.head == None:
            return
        
        t = self.head

        while(t.next !=None):
            t = t.next

        t.next = self.head
        self.head.prev = t

    def printDLL(self):
        if self.head == None:
            return
        
        t = self.head

        while True:
            print(t.data , end="<--->")
            t = t.next

            if t == self.head:
                break
        print(t.data)


obj = DoublyLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)
obj.insertAtBeg(5)
obj.insertAtMid(50 , 20 )
obj.deletionInDLL(40)
obj.circularLL()
obj.printDLL()