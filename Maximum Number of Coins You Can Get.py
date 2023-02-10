class Solution:
    def maxCoins(self, piles):        
        piles.sort(reverse=True)
        n = len(piles) // 3
        chosen = [[piles[2*i], piles[2*i+1], piles[-i-1]] for i in range(n)]
        return sum([x[1] for x in chosen])