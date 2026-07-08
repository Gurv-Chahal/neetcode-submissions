class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # we solve this problem using read/write pointers
        # both move in the same direction and one overwrites array as you go
        # k starts equal and falls behind as you reassign numbers

        k = 0

        # iterate over array
        for i in range(len(nums)):

            # if the current position does not equal the value
            if nums[i] != val:
                # assign the k index the ith index value which moves the non-value into an earlier position in the array
                nums[k] = nums[i]
                # iterate k forwards
                k += 1

        # return k
        return k

        
