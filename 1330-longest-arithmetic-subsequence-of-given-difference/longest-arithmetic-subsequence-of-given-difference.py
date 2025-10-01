class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        for num in arr:
            if num-difference in dp:
                dp[num]=1+dp[num-difference]
            else:
                dp[num]=1

        return max(dp.values())



            