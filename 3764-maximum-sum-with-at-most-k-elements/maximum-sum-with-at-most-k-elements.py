class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # grid.sort(key=lambda x:x)
        for g in grid:
            g.sort(reverse=True)
        print(grid)
        min_heap=[]
        for i in range(len(grid)):
            min_heap.extend(grid[i][:limits[i]])
        print(min_heap)
      
        heapq.heapify(min_heap)
        while min_heap and len(min_heap)>k:
            
            heapq.heappop(min_heap)
        return  sum(min_heap)
            

        