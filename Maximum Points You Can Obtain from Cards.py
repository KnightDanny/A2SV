class Solution:
  def maxScore(self, cardPoints, k):
    n, total = len(cardPoints), sum(cardPoints)
    w_total = sum(cardPoints[:n - k])
    output = total - w_total
    for i in range(k):
      w_total -= cardPoints[i]
      w_total += cardPoints[i + n - k]
      output = max(output, total - w_total)
    return output
