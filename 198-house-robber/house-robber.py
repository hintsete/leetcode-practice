class Solution:
    def rob(self, nums: List[int],memo=None) -> int:
        # memo={}
        # def dp(i):
        #     if i>=len(nums):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     memo[i]=max(nums[i]+dp(i+2),dp(i+1))
        #     return memo[i]

        # return dp(0)
        memo={}
        def dp(i):
            if i==0:
                return nums[0]

            if i==1:
                return max(nums[0],nums[1])

            if i in memo:
                return memo[i]
            memo[i]=max(nums[i]+dp(i-2),dp(i-1))
            return memo[i]

        return dp(len(nums)-1)

        

        
        