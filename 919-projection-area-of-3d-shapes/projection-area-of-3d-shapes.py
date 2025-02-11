class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res=0
        # this is for the x-y dimension
        # for num in grid:
        #     if num.count(0)==0:
        #         res+=len(num)
        #     elif  num.count(0)==1:
        #         res+=len(num)-1
        #     elif num.count(0)==2:
        #         res=0
        # print(res)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    res+=1

      
            
            

        for i in range(len(grid)):
            res+=max(grid[i])
        print(res)
        # res+=sum(max(grid))
        print(res)
        for i in range(len(grid)):
            m=0
            for j in range(len(grid[0])):
                m=max(m,grid[j][i])
            res+=m
            # print(res)
        print(res)

        return res
        

    
