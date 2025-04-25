class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    # isWater[i][j] = 0
                    queue.append((i,j))
                    visited.add((i,j))
                    # isWater[i][j] = 0
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        def inbound(r,c):
            return 0<=r<n and 0<=c<m

        level = 0
        while queue:
            curr_level = len(queue)
            for i in range(curr_level):
                x, y = queue.popleft()
                isWater[x][y] = level
                for dx,dy in direction:
                    new_x = dx + x
                    new_y = dy + y
                    if inbound(new_x,new_y) and (new_x,new_y) not in visited and isWater[new_x][new_y]==0:
                
                        queue.append((new_x,new_y))
                        visited.add((new_x,new_y))
            level += 1

               
        return isWater
        


        