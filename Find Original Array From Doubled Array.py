class Solution:
  def findOriginalArray(self, changed):
    output , collection  = [] , collections.deque()
    for num in sorted(changed):
      if collection and num == collection[0]: collection.popleft()
      else:
        collection.append(num * 2)
        output.append(num)
    return [] if collection else output