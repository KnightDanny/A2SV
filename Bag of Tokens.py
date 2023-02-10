class Solution:
  def bagOfTokensScore(self, tokens, power):
    output , score , i = 0, 0, collections.deque(sorted(tokens)) 

    while i and (power >= i[0] or score):
      while i and power >= i[0]:
        power -= i.popleft()
        score += 1
        
      output = max(output, score)
      
      if i and score:

        power += i.pop()
        score -= 1

    return output