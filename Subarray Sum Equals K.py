class Solution:
  def subarraySum(self, nums,k):
    output, prefix, tally = 0, 0, collections.Counter({0: 1})
    for num in nums:
      prefix += num
      output += tally[prefix - k]
      tally[prefix] += 1

    return output