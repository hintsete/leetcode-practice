class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)     
        m = len(mat[0]) 
        direction = [[-1,0],[1,0],[0,-1],[0,1]]    
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        queue = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
               
                
       
    
        while queue:
            r,c = queue.popleft()
        
            for dx,dy in direction:
                new_x = r + dx
                new_y = c + dy
                if inbound(new_x,new_y) and (new_x,new_y) not in visited:
                    mat[new_x][new_y] = mat[r][c] + 1
                    queue.append((new_x,new_y))
                    visited.add((new_x,new_y))
                
        return mat