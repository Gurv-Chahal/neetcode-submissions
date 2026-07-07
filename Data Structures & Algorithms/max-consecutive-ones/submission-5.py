# Optimal Solution - Also O(N) time complexity, O(1) Space complexity
# Note - use max() where possible 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter = 0
        highest_value = 0
        
        for num in nums:
            if num == 1:
                counter += 1
                # max() only updates when counter is bigger
                # no need for an extra if condition, use max instead
                highest_value = max(highest_value, counter)
            else:
                counter = 0

        return highest_value