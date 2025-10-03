class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # total=sum(nums)
        # target=total//2
        # memo={}
        # if total%2!=0:
        #     return False
        # def dp(target,i):
        #     if target==0:
        #         return True

        #     if target<0 or i>=len(nums):
        #         return False
        #     if(target,i) in memo:
        #         return memo[(target,i)]
        #     memo[(target,i)]=dp(target-nums[i],i+1) or dp(target,i+1)
        #     return memo[target,i]
        # return dp(target,0)
        total=sum(nums)
        target=total//2
        n=len(nums)
        if total%2!=0: return False
        dp=[[False]*(target+1) for _ in range(len(nums)+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1, n+1):
            for j in range(1,target+1):
                if j-nums[i-1]>=0:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][target]


            
        