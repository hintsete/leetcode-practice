class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr=[]
        for num in nums:
            if -num not in arr:
                heapq.heappush(arr,-num)

        print(arr)
        for _ in range(2):
            if arr:
                heapq.heappop(arr)
            else:
                return max(nums)

        if arr:
            return -(heapq.heappop(arr))
        else:
            return max(nums)
