



class stack:
    def __init__(self):
        self.__stack = []
    def push (self,val): #self means the "value" from the class and value is an outside value
        self.__stack.append(val)
    def pop(self): 
      value = self.__stack[-1]  #this will get the last element of the stack
      del self.__stack[-1] #this will delete the last element of the stack
      return value
    def printStack (self):
        print(self.__stack)
        for i in reversed(self.__stack):
            print(i)
        
class AddingStack(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum = 0
    def push(self, val):
        self.__sum += val 
        stack.push(self,val)
    def pop(self):
        value = stack.pop(self)
        self.__sum -= value
        return value


childStack = AddingStack()


#print (AddingStack.__dict__)
childStack.push(10)
childStack.push(10)
childStack.push(2)

print(childStack.__dict__)

childStack.pop()

print(childStack.__dict__)



# stackobject.push(10)
# stackobject.push(20)
# stackobject.push(30)
# stackobject.pop()



#stackobject.printStack()



# def push (one):
#     stack.append(one)
# push(5858)
# push(10)
# push(20)
# print(stack)

# def pop(): 
#     value = stack[-1]  #this will get the last element of the stack
#     del stack[-1] #this will delete the last element of the stack
#     return value

# print(pop())  # This will remove and return the last element of the stack
# print (stack)  #this will print the stack after the pop operation




