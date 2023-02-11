class Solution:
  def leastInterval(self, tasks, n):
    tally = collections.Counter(tasks)
    maximum_frequency = max(tally.values())
    maximum_frequencyTask = (maximum_frequency - 1) * (n + 1)
    num_maximum_frequency = sum(value == maximum_frequency for value in tally.values())
    return max(maximum_frequencyTask + num_maximum_frequency, len(tasks))