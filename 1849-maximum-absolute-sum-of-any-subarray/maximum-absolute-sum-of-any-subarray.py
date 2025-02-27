class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum=0
        min_val=0
        max_val=0
        res=0
        for num in nums:
            curr_sum+=num
            res=max(res,abs(curr_sum-max_val),abs(curr_sum-min_val))
            max_val=max(curr_sum,max_val)
            min_val=min(curr_sum,min_val)
        return res
        