class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        

    
class Stack:

    def __init__(self):
        self.top = None
       


    def push(self,data):
        newNode = Node(data,self.top)
        self.top = newNode
        

    
    def pop(self):
        if self.top is None:
            return "Underflow"
        self.top = self.top.next


    def peek(self):
        if self.top is None:
            return "Underflow"
        return self.top.data
    

    def isEmpty(self):
        if(self.top is None):
            return True
        return False
    

    def display(self):
        if(self.top is None):
            return "Stack is Empty"
        else:
            current = self.top
            while(current):
                print(current.data)
                current = current.next


S = Stack()
S.push(0)
S.push(1)
S.push(2)
S.display()
S.pop()
S.display()
        
    

