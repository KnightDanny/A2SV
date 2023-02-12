class Solution:
  def validateStackSequences(self, pushed, popped):
    stack = []
    for x in pushed:
      stack.append(x)
      while stack and stack[-1] == popped[i]:
        stack.pop()
        i += 1
    return not stack