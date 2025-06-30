class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr= [1]*numOnes + [0] * numZeros + [-1] * numNegOnes
        print(arr)
        max_heap=[]
        for num in arr:
            heapq.heappush(max_heap,-num)

        print(max_heap)
        total=0
        for i in range(k):
            total+= -(heapq.heappop(max_heap))

        return total

        