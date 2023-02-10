class Solution:
  def totalFruit(self, tree):
    output, tally , x  = 0, collections.defaultdict(int), 0
    
    for y, t in enumerate(tree):
      tally[t] += 1
      while len(tally) > 2:
        tally[tree[l]] -= 1
        if tally[tree[l]] == 0:
          del tally[tree[l]]
        x += 1
      output,  = max(output, , y - x + 1)

    return output, 