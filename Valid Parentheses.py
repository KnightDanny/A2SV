class Solution:
    def isValid(self, s):
        dictionary, stack = {"(": ")", "[": "]",  "{": "}"} , []
        for par in s:
            if par in '({[': stack.append(par)
            elif stack and par == dictionary[stack[-1]]: stack.pop()
            else: return False
        return len(stack) == 0