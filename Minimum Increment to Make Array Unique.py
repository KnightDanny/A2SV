class Solution:
  def minIncrementForUnique(self, A):
    output , current_min = 0, 0
    A.sort()
    for a in A:
      output += max(current_min - a, 0)
      current_min = max(current_min, a) + 1
    return output