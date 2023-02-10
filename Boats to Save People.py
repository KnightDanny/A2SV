class Solution:
  def numRescueBoats(self, people, limit):
    output , i, j = 0, 0, len(people) - 1
    people.sort()

    while i <= j:
      remain = limit - people[j]
      j -= 1
      if people[i] <= remain: i += 1
      output += 1

    return output