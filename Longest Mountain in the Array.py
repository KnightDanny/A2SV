class Solution:
  def longestMountain(self, A):
    output , i = 0

    while i + 1 < len(A):
      while i + 1 < len(A) and A[i] == A[i + 1]:
        i += 1

      add = 0
      sub = 0

      while i + 1 < len(A) and A[i] < A[i + 1]:
        add += 1
        i += 1

      while i + 1 < len(A) and A[i] > A[i + 1]:
        sub += 1
        i += 1

      if add > 0 and sub > 0: output = max(output, add + sub + 1)

    return output