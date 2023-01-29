class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tally = 0
        for i in range(len(nums)):
            
            for j in range(len(nums)):
               
                if nums[i] == nums[j] and i < j:
                    tally += 1
        return tally