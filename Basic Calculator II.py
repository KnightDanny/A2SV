class Solution:
  def calculate(self, s):
    if not s:
        return "0"
    stack, number, op = [], 0, "+"
    for i in xrange(len(s)):
        if s[i].isdigit():
            number = number*10+ord(s[i])-ord("0")
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if op == "-":stack.append(-number)
            elif op == "+": stack.append(number)
            elif op == "*": stack.append(stack.pop()*number)
            else:
                temp = stack.pop()
                if temp//number < 0 and temp%number != 0: stack.append(temp//number+1)
                else: stack.append(temp//number)
            op = s[i]
            number = 0
    return sum(stack)