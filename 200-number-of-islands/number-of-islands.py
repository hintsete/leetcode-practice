class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n , m = len(grid) , len(grid[0])

        def dfs(r,c):
            if r >= n or c >= m or r < 0 or c < 0 or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                dfs(r , c-1)
                dfs(r , c+1)
                dfs(r-1 , c)
                dfs(r+1 , c)


        island=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i,j)
            
        return island
     

        