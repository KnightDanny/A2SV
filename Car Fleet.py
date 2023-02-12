class Solution:
  def carFleet(self, target, position, speed):
    output, maximum = 0
    times = [float(target - p) / s for p, s in sorted(zip(position, speed),reverse = True)] 
    for time in times:
      if time > maximum:
        maximum = time
        output += 1

    return output
