class Stack:
    def __init__(self,size):
        self.size = size
        self.top = -1
        self.stack = [None]*size
    

    def push(self,data):
        if(self.top==self.size-1):
            print("Overflow")
        else:
            self.top +=1
            self.stack[self.top] = data


    def pop(self):
        if(self.top== -1):
            return "Underflow"
        else:
            val = self.stack[self.top]
            self.stack[self.top] = None
            self.top -=1
            return val
        


    def peek(self):
        if(self.top==-1):
            return "Stack empty"
        else:
            return self.stack[self.top]
        

    def isEmpty(self):
        if (self.top==-1):
            return True
        return False
    
    def isFull(self):
        if (self.top==self.size-1):
            return True
        return False

    def display(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])

    def length(self):
        return self.top+1

S = Stack(10)
S.push(0)
S.push(1)
S.push(2)
S.push(3)
S.display()
print(S.pop())
S.display()
print(S.length())


    