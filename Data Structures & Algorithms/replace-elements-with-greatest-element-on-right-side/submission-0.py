class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # Time: O(N), Space: O(1)

        rightMax = -1
        # range(start, stop, step)
        # starts at the end (included), python is 0-indexed
        # stop - this is the index to stop at (excluded)
        for i in range(len(arr) - 1, -1, -1):
            original = arr[i] # hold the current element
            arr[i] = rightMax # set the current element to the highest element seen so far
            rightMax = max(original, rightMax) # update rightMax

        return arr
