class Solution:
  def findTheWinner(self, n, k):
    friends, tally, pointer = [False] * n, n, 0 
    while tally > 1:
      for _ in range(k):
        while friends[pointer % n]: pointer += 1  
        pointer += 1
      friends[(pointer - 1) % n] = True
      tally -= 1
    pointer = 0
    while friends[pointer]: pointer += 1

    return pointer + 1