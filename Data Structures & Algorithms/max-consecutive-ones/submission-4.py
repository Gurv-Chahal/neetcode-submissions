# My Solution: O(N) time complexity, O(1) Space complexity

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # create two variables
        # one to track the current counter and another to track highest counter
        counter = 0;
        highest_value = 0;

        # iterate over the arraya and whenever 1 appears update the counter
        for i in range(len(nums)):
            if (nums[i] == 1):
                counter += 1
                # if counter becomes higher than highest counter then update it
                if (counter > highest_value):
                    highest_value = counter
            # if 1 doesn't appear then set counter to 0 again
            else:
                counter = 0

        return highest_value