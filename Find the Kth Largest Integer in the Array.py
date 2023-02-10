class Solution(object):
    def kthLargestNumber(self, nums, k):
       
       output = []

       for num in nums:
           output.append(int(num))

       output.sort()
       return str(output[k * -1])
