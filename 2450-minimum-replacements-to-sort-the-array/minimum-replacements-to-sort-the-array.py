class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        bound=nums[n-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>bound:
                part=(nums[i]+bound-1)//bound

                count+=part-1
                bound=nums[i]//part
            else:
                bound=nums[i]
            
                
        return count