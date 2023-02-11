class Solution:
  def dailyTemperatures(self, temperatures):
    output, stack = [0] * len(temperatures) , []

    for i, t in enumerate(temperatures):
      while stack and t > temperatures[stack[-1]]:
        index = stack.pop()
        output[index] = i - index
      stack.append(i)

    return output