class Solution:
  def maxArea(self, height):
    output, length, limit = 0, 0, len(height) - 1
    while length < limit:
      minimum = min(height[length], height[limit])
      output = max(output, minimum * (limit - length))
      if height[length] < height[limit]: length += 1
      else: limit -= 1
      
    return output