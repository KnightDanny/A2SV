class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        def check(nums):
            nums_set = frozenset(nums)
            if len(nums_set) != len(nums):
                return len(nums_set) == 1
            maximum, minumum, = max(nums), min(nums)
            step = (maximum - minumum) // (len(nums) - 1)
            return all((i in nums_set for i in range(minumum, maximum, step)))
        return [check(nums[i:j + 1]) for i, j in zip(l, r)]