class Solution:

    # O(N) Time and Space complexity
    def calPoints(self, operations: List[str]) -> int:
        
        # create a new array to hold the scores
        scores = []

        # iterate over given array
        for i in range(len(operations)):
          

          # operation is + so add the previous two indices in SCORE array
          # do not use scores[i] because that doesn't exist yet, only exists in operations[]
          if operations[i] == '+':
            scores.append(scores[-1] + scores[-2])

          # operation D means double the previous index in score and append it
          elif operations[i] == 'D':
            scores.append(scores[-1] * 2)

          # delete the previous score from the array, here we can use .pop() to do that
          # since a stack is implemented with an array
          elif operations[i] == 'C':
            scores.pop()

          # otherwise there is no operation and it is a number
          else:
            # we are going to turn the string into a number using int() then append it
            scores.append(int(operations[i]))


        # We want to return the sum of the array, so we can use sum() to do that
        return sum(scores)