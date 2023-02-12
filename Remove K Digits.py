class Solution:
    def removeKdigits(self, num, k):
        trials, stack = k, []
        for n in num:
            while stack and n < stack[-1] and trials > 0:
                stack.pop()
                trials -= 1
            stack.append(n)
        output = "".join(stack[0:len(num)-k]).lstrip("0")
        return "0" if output == "" else output