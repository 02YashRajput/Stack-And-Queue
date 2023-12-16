class Priority_Queue:
    def __init__(self,size):
        self.size = size
        self.queue = []
        self.front = self.rear = -1
    def isEmpty(self):
        if self.front == -1 or self.front>self.rear:
            return True
        return False
    
    def isFull(self):
        if (self.rear+1-self.front) ==self.size:
            return True
        return False

    def EnQueue(self,value,priority):
        if self.isFull():
            print("Overflow!!!")
            return
        elif self.front == self.rear == -1:
            self.front =0
        self.queue.append((value,priority))
        self.queue = sorted(self.queue, key=lambda x: (x[1] is not None, x[1]))
        self.rear +=1

    def DeQueue(self):
        if self.isEmpty():
            print("Underflow!!!")
            return
        self.front+=1
        val = self.queue[0][0]
        self.queue.pop(0)
        return val


    def display(self):
        for i in range(len(self.queue)):
            print(self.queue[i][0])
        print()


Q = Priority_Queue(5)
Q.EnQueue(1,1)
Q.EnQueue(0,0)
Q.EnQueue(5,5)
Q.EnQueue(3,3)
Q.EnQueue(4,4)
Q.display()
print("deleted value:",Q.DeQueue())
Q.display()
Q.EnQueue(2,2)
Q.display()
