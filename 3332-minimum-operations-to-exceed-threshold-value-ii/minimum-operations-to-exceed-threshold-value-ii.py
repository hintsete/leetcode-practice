class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        heapq.heapify(nums)
        
        while nums[0]<k and len(nums)>=2:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            heapq.heappush(nums,(2*x)+y)
            count+=1
        return count
            
        