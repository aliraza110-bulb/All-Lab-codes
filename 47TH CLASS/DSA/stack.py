class Stack:
    def __init__(self,size:int):
        self.max_size=size
        self._data=[None]*size
        self.top=-1
    def is_empty(self) -> bool:
        return self.top == -1 
    def is_full(self) -> bool:
        return self.top == self.max_size - 1
    def push(self,value=any) ->bool:
        if self.is_full():
            print("Stack overflow can not push {value}")
            return False
        self.top +=1
        self._data[self.top]=value
        return True
    def peek(self):
        if self.is_empty():
            print("Stack underflow stack is empty")
            return None
        return self._data[self.top]
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow! Stack is empty.")
            return None

        value = self._data[self.top]
        self._data[self.top] = None
        self.top -= 1
        return value
    
if __name__ == "__main__":
    s=Stack(5)
    print("Empty",s.is_empty())
    s.push(10)
    s.push(20)
    s.push(30)
    print("Peek ELement ",s.peek())
    print("Removing element",s.pop())