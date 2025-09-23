class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
       
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        memo = {}
        
        def dp(i, target):
          
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            
         
            if (i, target) in memo:
                return memo[i, target]
            
           
            memo[i, target] = dp(i+1, target - nums[i]) or dp(i+1, target)
            return memo[i, target]
        
        return dp(0, target)

            
        