class Solution(object):
    def merge(self, intervals):
        
        output = []
        intervals.sort()
        
        for i in intervals:
            if len(output) == 0 or output[-1][1] < i[0]:
                output.append(i)
            else:
                output[-1][1] = max(output[-1][1],i[1])
        return output