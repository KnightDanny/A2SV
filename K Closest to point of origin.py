class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for x,y in points:
            distance = (x**2) + (y**2)
            heap.append([distance, x, y])
        
        heapq.heapify(heap)
        output  = []
        
        while k > 0:
            distance, x , y = heapq.heappop(heap)
            output.append([x,y])
            k -= 1
        return output