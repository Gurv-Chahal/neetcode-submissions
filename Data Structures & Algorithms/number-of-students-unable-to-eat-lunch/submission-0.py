from collections import deque

# Not Optimal Solution
# O(N)^2 time complexity because you can process the same students twice
# you may perform N rotations for N sandwiches
# O(N) - space complexity

# deque operations
# popleft() - remove from front
# append() - add to back
# pop() - remove from back
# appendleft() - add to front 

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # create two queues
        # deque(list) copies the list into the new deque
        studentQueue = deque(students)
        sandwichQueue = deque(sandwiches)

        # use a counter that records how many students have rejected the current sandwich consecutively
        rejections = 0
        
        # keep going until rejections reaches the length of the queue
        while(rejections < len(studentQueue)):
            
            # if first student likes first sandwich pop them both off stack
            if (studentQueue[0] == sandwichQueue[0]):
                studentQueue.popleft()
                sandwichQueue.popleft()

                # restart the count
                rejections = 0 

            # otherwise pop student and add to back of line
            else:
                # remove the front value of the queue
                student = studentQueue.popleft()
                # append it to the new queue to the end
                studentQueue.append(student)

                rejections += 1

        return len(studentQueue)












