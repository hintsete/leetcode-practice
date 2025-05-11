class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        my_dict={
             1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(1, 0), (0, 1)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
            
        }
        reverse={
            (0,-1):(0,1),
            (0,1):(0,-1),
            (-1,0):(1,0),
            (1,0):(-1,0)
        }
        n=len(grid)
        m=len(grid[0])
        def inbound(r,c):
            return 0<=r<n and 0<=c<m

        parent={}
        
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                parent[p2]=p1
        for i in range(n):
            for j in range(m):
                parent[(i,j)]=(i,j)

        for r in range(n):
            for c in range(m):
                for dx,dy in my_dict[grid[r][c]]:
                    new_r=r+dx
                    new_c=c+dy

                    if inbound(new_r,new_c):
                        if reverse[dx,dy] in my_dict[grid[new_r][new_c]]:
                            union((r,c),(new_r,new_c))

        return find((0,0))==find((n-1,m-1))
                