class Converter:
    def __init__(self):
        self.output = []
        self.temp = []
        self.top= -1
        self.priority = {'+':1,'-':1,'*':2,'/':2,'^':3}


    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.temp[self.top] if not self.isEmpty() else None
    
    def push(self,value):
        self.temp.append(value)
        self.top += 1

    def pop(self):
        if self.top !=-1:
            self.top -=1
            return self.temp.pop()
        else:
            return None
    
    def notGreater(self,i):
        try: 
            a = self.priority[i]
            b = self.priority[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
        
    
    def infixToPostfix(self,exp):

        for i in exp:
            if i.isalpha():
                self.output.append(i)

            elif i =='(':
                self.push(i)

            elif i == ')':
                while(not self.isEmpty() and self.peek() != '('):
                    self.output.append(self.pop())
                if(not self.isEmpty() and self.peek() != '('):
                    return self.pop()
                else:
                    self.pop()

            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while(not self.isEmpty() ):
            self.output.append(self.pop())
        
        for i in self.output:
            print(i,end = "")

    def infixToPrefix(self,exp):

        for i in exp[::-1]:
            if i.isalpha():
                self.output.append(i)

            elif i ==')':
                self.push(i)

            elif i == '(':
                while(not self.isEmpty() and self.peek() != ')'):
                    self.output.append(self.pop())
                if(not self.isEmpty() and self.peek() != ')'):
                    return self.pop()
                else:
                    self.pop()

            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while(not self.isEmpty() ):
            self.output.append(self.pop())
        
        for i in self.output[::-1]:
            print(i,end = "")	


    def postfixToInfix(self,exp):
        for i in exp:
            if i.isalpha():
                self.output.insert(0,i)
            else:
                op1 = self.output[0]
                self.output.pop(0)
                op2 = self.output[0]
                self.output.pop(0)
                self.output.insert(0,"(" + op2 + i + op1 + ")")

        print(self.output[0])


    def prefixToInfix(self,exp):
        for i in exp[::-1]:
            if i.isalpha():
                self.output.insert(0,i)
            else:
                op1 = self.output[0]
                self.output.pop(0)
                op2 = self.output[0]
                self.output.pop(0)
                self.output.insert(0,")" + op2 + i + op1 + "(")

        ch= self.output[0]
        print(ch[::-1])




exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Converter()
obj.infixToPostfix(exp)
print()

obj1 = Converter()
obj1.infixToPrefix(exp)
print()     

exp = "abcd^e-fgh*+^*+i-"
obj2 = Converter()
obj2.postfixToInfix(exp)

exp = "+a-*b^-^cde+f*ghi"
obj3 = Converter()
obj3.prefixToInfix(exp)

    