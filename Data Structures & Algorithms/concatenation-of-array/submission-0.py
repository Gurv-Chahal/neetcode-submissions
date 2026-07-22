class Solution:
    # O(N) time and space complexity
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # create array. 
        ans = []

        # loop through the array once and append each element
        for i in range(len(nums)):
            ans.append(nums[i])

        # loop through array again and append each element
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans