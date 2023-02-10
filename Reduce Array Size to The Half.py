class Solution:
  def minSetSize(self, arr):
    n = len(arr)
    count = collections.Counter(arr).most_common()
    count.sort(key=lambda c: -c[1])
    total = 0
    for i, c in enumerate(count):
      total += c[1]
      if total >= n // 2:
        return i + 1