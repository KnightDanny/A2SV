class Solution:
  def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
    def second(x, y):
      n = len(nums)
      left = [0] * n
      incr = 0

      for i in range(n):
        incr += nums[i]
        if i >= x: incr -= nums[i - x]
        if i >= x - 1: left[i] = max(left[i - 1], incr) if i > 0 else incr
        
      right = [0] * n
      incr = 0

      for i in reversed(range(n)):
        incr += nums[i]
        if i <= n - y - 1: incr -= nums[i + y]
        if i <= n - y: right[i] = max(right[i + 1], incr) if i < n - 1 else incr

      return max(left[i] + right[i + 1] for i in range(n - 1))

    return max(second(firstLen, secondLen), second(secondLen, firstLen))