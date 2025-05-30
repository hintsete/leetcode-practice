class MedianFinder:

    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]
        

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            moved_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved_num)
        elif len(self.min_heap) > len(self.max_heap):
            moved_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved_num)
        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()