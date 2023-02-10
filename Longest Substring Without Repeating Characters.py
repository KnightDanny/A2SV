class Solution:
  def lengthOfLongestSubstring(self, s):
    output, tally, x = 0, collections.Counter(), 0

    for y, char in enumerate(s):
      tally[char] += 1
      while tally[char] > 1:
        tally[s[x]] -= 1
        x += 1
      output = max(output, y - x + 1)

    return output