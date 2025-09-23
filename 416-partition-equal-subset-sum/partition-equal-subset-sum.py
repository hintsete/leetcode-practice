class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        target=total//2
        memo={}
        if total%2!=0:
            return False
        def dp(target,i):
            if target==0:
                return True

            if target<0 or i>=len(nums):
                return False
            if(target,i) in memo:
                return memo[(target,i)]
            memo[(target,i)]=dp(target-nums[i],i+1) or dp(target,i+1)
            return memo[target,i]
        return dp(target,0)

            
        