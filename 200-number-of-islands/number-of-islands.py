class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction=[[-1,0],[1,0],[0,-1],[0,1]]
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        visited=set()


        def dfs(r,c):
            if not inbound(r,c) or (r,c)  in visited or grid[r][c]=="0" :
                return 0

            ans=int(grid[r][c])
            visited.add((r,c))
            for dx,dy in direction:
                new_r=dx+r
                new_c=dy+c
                dfs(new_r,new_c)
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    res+=1
                    dfs(i,j)
        return res

            

        