class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=set()
        direction=[[-1,0],[0,-1],[1,0],[0,1]]
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        perimeter=0
        def dfs(visited,row,col):
            nonlocal perimeter
            visited.add((row,col))
            for r,c in direction:
                new_r=row+r
                new_c=col+c
                if inbound(new_r,new_c)  and grid[new_r][new_c]:
                    if  (new_r,new_c) not in visited:
                        dfs(visited,new_r,new_c)
                else:
                    perimeter+=1
            

                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and (r,c) not in visited:
                    dfs(visited,r,c)
                    return perimeter
                
        return perimeter


            
            # return self.perimeter
            # if grid[row][col]==1:
            #     # self.perimeter=
            #     self.perimeter+=
            #     def
        # return dfs(set(),0,0)

            
           
