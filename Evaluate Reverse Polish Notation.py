class Solution:
    def evalRPN(self, tokens):
        hashdiction = {"+": add, "-": sub, "*": mul, "/":lambda a,b: int(a/b)}
        stack = []
        for token in tokens:
            if token in hashdiction:
                y = stack.pop()
                x = stack.pop()
                z = hashdiction[token](x, y)
            else:
                z = int(token)
            stack.append(z)
        return stack[-1]