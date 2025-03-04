class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # possible subset 2**(len(nums)-1)
        i=0
        patches=0
        min_val=1
        while min_val<=n:
            if i<len(nums) and nums[i]<=min_val:

                min_val+=nums[i]
                i+=1
            else:
                min_val+=min_val
                patches+=1

        return patches
       

        