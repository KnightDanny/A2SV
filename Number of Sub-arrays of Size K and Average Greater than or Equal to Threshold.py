class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        def sums(arr,k):
            start, running_total, n, output = 0, 0, len(arr), [0]*(n-k+1)
            for x in range(n):
                running_total += arr[x]
                while x - start == k-1:
                    output[start] = running_total / k 
                    running_total -= arr[start]
                    start += 1
            return output
        tally = 0
        for i in sums(arr,k):
            if i >= threshold:
                tally += 1
        return tally