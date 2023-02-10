class Solution:
  def pancakeSort(self, arr):
    output = []

    for target in range(len(arr), 0, -1):
      i = arr.index(target)
      arr[:i + 1] = arr[:i + 1][::-1]
      arr[:target] = arr[:target][::-1]
      output.append(i + 1)
      output.append(target)
    return output