class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        unique=set(nums)
        l=0
        n=len(nums)
        window=defaultdict(int)
        req=len(unique)
        for r in range(len(nums)):
            window[nums[r]]+=1
            while len(window)==req:
                count+=n-r
                window[nums[l]]-=1
                if window[nums[l]]==0:
                    del window[nums[l]]
                l+=1
            



        return count
        