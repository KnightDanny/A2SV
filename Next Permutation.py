class Solution:
  def nextPermutation(self, nums):
    n = len(nums)
    i = n - 2
    while i >= 0:
      if nums[i] < nums[i + 1]: break
      i -= 1
    if i >= 0:
      for j in range(n - 1, i, -1):
        if nums[j] > nums[i]:
          nums[i], nums[j] = nums[j], nums[i]
          break

    def reverse(nums,x,y):
      while x < y:
        nums[x], nums[y] = nums[y], nums[x]
        x += 1
        y -= 1
    reverse(nums, i + 1, len(nums) - 1)