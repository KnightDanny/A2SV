class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final = []
        nums.sort()
        
        for x in range(len(nums)):
            
            if nums[x] == target:
                final.append(x)
        
        return finall