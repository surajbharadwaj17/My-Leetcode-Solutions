class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.out_stack) == 0:
            while(len(self.in_stack) > 0):
                self.out_stack.append(self.in_stack.pop())
        ret = self.out_stack.pop()
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.out_stack) == 0:
            print(self.in_stack)
            while(len(self.in_stack)>0):
                self.out_stack.append(self.in_stack.pop())  
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.out_stack) == 0 and len(self.in_stack) == 0:
            return True
        else:
            return False
        