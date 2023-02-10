class Solution:
    def hIndex(self, citations):
        citations.sort()
        n , output = len(citations) , 1
        while output <= n:
            if(citations[n-output]<output): break
            output=output + 1
        
            
        return output- 1