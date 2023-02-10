class Solution:
  def rotate(self, nums, k):
    k %= len(nums)
    self.reverse(nums, 0, len(nums) - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, len(nums) - 1)

  def reverse(self, nums, x, y):
    while x < y:
      nums[x], nums[y] = nums[y], nums[x]
      x += 1
      y -= 1