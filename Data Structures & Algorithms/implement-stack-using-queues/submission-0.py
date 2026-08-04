class MyStack:

  # Not optimal solution

  # only operations we are allowed to use in this problem
  # queue.append(x)       add to back
  # queue.popleft()       remove from front
  # queue[0]              view front
  # len(queue)            size

  # queue = [oldest, ... , newest] -> order of removal [first, ... , last]
  # top = newest element added

    from collections import deque

    def __init__(self):

        # main queue
        self.queue1 = deque()

        # duplicate temporary queue - may need later
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:

        # iterate over every item in queue 1 except the back of the queue (top of stack)
        for i in range(len(self.queue1) - 1):
          # pop and save element from q1
          element = self.queue1.popleft()
          # append it to q2
          self.queue2.append(element)

        # pop the remaining element off the main queue and save it
        savedElement = self.queue1.popleft()

        # swap the queues again
        for i in range(len(self.queue2)):
          # pop and save element from q2
          element = self.queue2.popleft()
          # append it to q1
          self.queue1.append(element)
        
        # return saved element
        return savedElement

    def top(self) -> int:

        # Move everything except the newest element into queue2
        for i in range(len(self.queue1) - 1):
          element = self.queue1.popleft()
          self.queue2.append(element)

        # Remove and save the newest element
        savedElement = self.queue1.popleft()

        # Put it back because top() should not remove it
        # puts it at the top of the stack or back of the queue again
        self.queue2.append(savedElement)

        # Move everything back into queue1 again
        for i in range(len(self.queue2)):
          element = self.queue2.popleft()
          self.queue1.append(element)

        # returns the element while keeping queue1 the same
        return savedElement

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()