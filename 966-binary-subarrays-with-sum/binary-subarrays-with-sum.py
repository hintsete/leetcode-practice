class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def calculator(y):
            if y<0:
                return 0
            left=0
            current_sum=0
            res=0
            for right in range(len(nums)):
                current_sum+=nums[right]
                while current_sum>y:
                    current_sum-=nums[left]
                    left+=1
                res+=(right-left+1)
            return res


        return calculator(goal)- calculator(goal-1)
        