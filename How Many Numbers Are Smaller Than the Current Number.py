class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final = []

        for x in range(len(nums)):
            tally = 0

            for y in range(len(nums)):

                if nums[y] < nums[x]:
                    tally += 1

            final.append(tally)
            
        return final