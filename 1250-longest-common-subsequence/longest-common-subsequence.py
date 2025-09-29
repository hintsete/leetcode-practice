class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        def dp(i,j):
            #base case
            if i>=len(text1) or j>= len(text2):
                return 0
            # print(i,j,memo)
            if (i,j) in memo:
                return memo[i,j]
            if text1[i]==text2[j]:
                memo[i,j]=1+dp(i+1,j+1)
            else:
                memo[i,j]=max(dp(i+1,j),dp(i,j+1))
            # memo[i,j]=max(1+dp(i+1,j+1),dp(i+1,j+1))


            # count=0
            return memo[i,j]
        

        return dp(0,0)
        