class Solution(object):
    def kthLargestNumber(self, nums, k):
       
       new_list = []

       for num in nums:
           new_list.append(int(num))

       new_list.sort()
       return str(new_list[k * -1])