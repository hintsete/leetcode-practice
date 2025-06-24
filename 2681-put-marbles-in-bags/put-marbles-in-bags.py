class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)
        pair=[]
        for i in range(n-1):
            pair.append(weights[i]+weights[i+1])

        print(pair)
        max_sum=0
        min_sum=0

        max_heap=[-p for p in pair]
        min_heap=pair[:]
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        for i in range(k-1):
            max_sum+= -(heapq.heappop(max_heap))
            min_sum+= heapq.heappop(min_heap)

        return max_sum-min_sum
        
        


        

        