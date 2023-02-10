class Solution:
    def longestSubarray(self, nums):
        output, left_pointer, x = 0, 0, 1
        for right_pointer in range(len(nums)):
            if nums[right_pointer] == 0: x -= 1
            if x < 0:
                if nums[left_pointer] == 0: x += 1
                left_pointer += 1
            output = max(output, right_pointer-left_pointer)
        return output