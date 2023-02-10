class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tally = 0
        nums.sort()

        for x in nums:
            
            for y in nums:
                
                if x + y == k:
                    tally += 1
                    nums.remove(x)
                    nums.remove(y)

        return tally