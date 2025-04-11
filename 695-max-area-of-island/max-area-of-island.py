class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_val = 0
        n , m = len(grid) , len(grid[0])
        def dfs(r,c):
            # nonlocal max_val
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c]==0:
                return 0
            # ans = grid[r][c]


            grid[r][c] = 0
            ans = 1
            ans += dfs(r , c - 1)
            ans += dfs(r , c + 1)
            ans += dfs(r - 1 , c)
            ans += dfs(r + 1 , c)

            return ans
            



        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area=dfs(i , j)
                    max_val=max(max_val , area)
        return max_val
        