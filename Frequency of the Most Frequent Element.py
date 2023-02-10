class Solution:
  def maxFrequency(self, nums,k):
    output , add = 0 , 0
    nums.sort()
    i = 0
    for x, num in enumerate(nums):
      add += num
      while add + k < num * (x - i + 1):
        add -= nums[i]
        i += 1
      output = max(output, x - i + 1)
    return output