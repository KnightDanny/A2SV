class Solution:
    def longestSubarray(self, nums, limit):
        minimum, maximum = deque(), deque()
        output, x, y = 0, 0, 0
        while y < len(nums):
            while minimum and nums[y] <= nums[minimum[-1]]: minimum.pop()
            while maximum and nums[y] >= nums[maximum[-1]]: maximum.pop()
            minimum.append(y)
            maximum.append(y)
            while nums[maximum[0]] - nums[minimum[0]] > limit:
                x += 1
                if x > minimum[0]: minimum.popleft()
                if x > maximum[0]: maximum.popleft()
            output = max(output, y - x + 1)
            y += 1
        return output