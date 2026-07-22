class MinStack:
    # O(1) Time Complexity
    # O(N) Space

    # basically a constructor that runs everytime an object is created
    def __init__(self):
        # self is used to access data belonging to the object -- in init
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # access stack from constructor and append
        self.stack.append(val)

        # if minstack is empty -> append
        if len(self.minStack) == 0:
            self.minStack.append(val)
        # use min() to compare val and previous element on minstack -> choose minimum
        else:
            self.minStack.append(min(val, self.minStack[-1]))


    def pop(self) -> None:
        # minstack method - different from just .pop() in python
        # pop both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # access the last element of the stack without removing it
        return self.stack[-1]

    def getMin(self) -> int:
        # access the last element on minstack
        return self.minStack[-1]
