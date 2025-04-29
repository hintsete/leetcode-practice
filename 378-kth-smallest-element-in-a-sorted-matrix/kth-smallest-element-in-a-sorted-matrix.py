class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap=[]
        for mat in matrix:
            for num in mat:
                min_heap.append(num)
        heapq.heapify(min_heap)
        for _ in range(k-1):
            heapq.heappop(min_heap)
        return heapq.heappop(min_heap)
    