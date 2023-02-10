class Solution:
  def pivotIndex(self, nums):
    total, prefix = sum(nums), 0
    for i, num in enumerate(nums):
      if prefix == total - prefix - num:
        return i
      prefix += num

    return -1