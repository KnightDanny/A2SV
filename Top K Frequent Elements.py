class Solution:
    def topKFrequent(self, nums, k):
        my_dictionary = {}
        for i in nums: my_dictionary[i] = my_dictionary.get(i,0) + 1
        return sorted(my_dictionary,key = my_dictionary.get,reverse=True)[0:k] 