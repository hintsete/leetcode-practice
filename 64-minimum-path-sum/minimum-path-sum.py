class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp=[[float("inf")]* m for _ in range(n)]
        dp[n-1][m-1]= grid[n-1][m-1]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i== n-1 and j==m-1:
                    continue

                down= dp[i+1][j] if i+1<n else float("inf")
                right= dp[i][j+1] if j+1<m else float("inf")
                dp[i][j]=min(down, right)+ grid[i][j]
        return dp[0][0]
        # memo = {}
        # def dp(i,j):
        #     if i >= n or j >= m:
        #         return float('inf')

        #     if (i,j) in memo:
        #         return memo[i,j]
        #     if i == n-1 and j == m-1:
        #         return grid[i][j]

        #     else:
        #         memo[i,j]=min(dp(i+1,j) ,dp(i,j+1)) + grid[i][j]

        #     return memo[i,j]

        # return dp(0,0)

        