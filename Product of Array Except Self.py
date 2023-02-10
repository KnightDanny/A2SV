class Solution:
  def productExceptSelf(self, nums):
    n = len(nums)
    prefix, suffix = [1] * n, [1] * n
    for i in range(1, n): prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in reversed(range(n - 1)): suffix[i] = suffix[i + 1] * nums[i + 1]
    return [prefix[i] * suffix[i] for i in range(n)]