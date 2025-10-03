class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memo={}
        # def dp(i,j):
        #     #base case
        #     if i>=len(text1) or j>= len(text2):
        #         return 0
        #     # print(i,j,memo)
        #     if (i,j) in memo:
        #         return memo[i,j]
        #     if text1[i]==text2[j]:
        #         memo[i,j]=1+dp(i+1,j+1)
        #     else:
        #         memo[i,j]=max(dp(i+1,j),dp(i,j+1))
        #     # memo[i,j]=max(1+dp(i+1,j+1),dp(i+1,j+1))


        #     # count=0
        #     return memo[i,j]
        

        # return dp(0,0)
        n=len(text1)
        m=len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    p1=dp[i-1][j] 
                    p2=dp[i][j-1] 
                    dp[i][j]=max(p1,p2)

        return dp[n][m]
        