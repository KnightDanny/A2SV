class Solution:
  def maxVowels(self, s, k):
    output , maximum , vowels = 0, 0, {'a', 'e', 'i', 'o', 'u'}
    for i, char in enumerate(s):
      if char in vowels: maximum += 1
      if i >= k and s[i - k] in vowels: maximum -= 1
      output = max(output, maximum)
    return output
