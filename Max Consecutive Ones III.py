class Solution:
  def longestOnes(self, A, K):
    output, x = 0, 0
    for y, a in enumerate(A):
      if a == 0: K -= 1
      while K < 0:
        if A[x] == 0: K += 1
        x += 1
      output = max(output, y - x + 1)
    return output