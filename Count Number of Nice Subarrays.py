class Solution:
  def numberOfSubarrays(self, nums,k):
    def numberOfSubarraysAtMost(k):
      output, x, y = 0, 0, 0
      while y <= len(nums):
        if k >= 0: 
          output += y - x
          if y == len(nums): break
          if nums[y] & 1: k -= 1
          y += 1
        else:
          if nums[x] & 1: k += 1
          x += 1
      return output
    return numberOfSubarraysAtMost(k) - numberOfSubarraysAtMost(k - 1)