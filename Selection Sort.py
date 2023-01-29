class Solution: 
    def select(self, arr, i):
        # code here
        
        maximum = arr[0]
        idx = 0
        
        for x in range(1,i+1):
            if arr[x] > maximum:
                idx = x
                maximum = arr[x]
        return idx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1, 0, -1):
            x = self.select(arr,i)
            arr[i], arr[x] = arr[x], arr[i]
        return arr
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends