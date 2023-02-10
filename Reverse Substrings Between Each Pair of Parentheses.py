class Solution:
  def reverseParentheses(self, s):
    output , stack , match = [] , [] , {}
    for i, x in enumerate(s):
      if x == '(':
        stack.append(i)
      elif x == ')':
        j = stack.pop()
        match[i] = j
        match[j] = i
    i = 0
    y = 1
    while i < len(s):
      if s[i] in '()':
        i = match[i]
        y = -y
      else: output.append(s[i])
      i += y
    return ''.join(output)
