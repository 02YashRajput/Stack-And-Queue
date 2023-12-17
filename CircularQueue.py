class CircularQueue():

	def __init__(self, size):
		self.size = size
		self.queue = [None for i in range(size)] 
		self.front = self.rear = -1

	def isFull(self):
		if ((self.rear + 1) % self.size == self.front):
			return True
		return False


	def isEmpty(self):
		if self.front ==-1:
			return True
		return False

	def enqueue(self, data):
		
		if self.isFull(): 
			print("Queue is Full\n")
			return
			
		elif (self.front == -1): 
			self.front = 0

		self.rear = (self.rear + 1) % self.size 
		self.queue[self.rear] = data
			
	def dequeue(self):
		if self.isEmpty(): 
			print ("Queue is Empty\n")
			return
			
		temp=self.queue[self.front]
		if (self.front == self.rear): 
			self.front = -1
			self.rear = -1
		else:
			self.front = (self.front + 1) % self.size
		return temp

	def display(self):
	
		if self.isEmpty(): 
			print ("Queue is Empty")

		elif (self.rear >= self.front):
			print("Elements in the circular queue are:",end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Elements in Circular Queue are:",end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		

ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()

