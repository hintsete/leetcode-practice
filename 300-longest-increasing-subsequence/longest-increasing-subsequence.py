class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            count=1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    count= max(dp(j)+1, count)
            return count

        return max (dp(i) for i in range(len(nums)))
