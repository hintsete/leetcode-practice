class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[]
        for num in nums:
            max_heap.append(-num)
        print(max_heap)
        heapq.heapify(max_heap)
        for _ in range(k-1):
            heapq.heappop(max_heap)
        largest=heapq.heappop(max_heap)
        return -largest
    
