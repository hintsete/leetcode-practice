class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        direction = [[-1,0],[1,0],[0,1],[0,-1]]
        ans=""
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        visited=set()
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            if not inbound(r,c) or (r,c) in visited or board[r][c]!=word[idx]:
                return False
            visited.add((r,c))
            for dx,dy in direction:
                if dfs(r+dx,c+dy,idx+1):
                    return True
            visited.remove((r,c))
            return False
            # visited.add((r,c))
            # if board[r][c] in word:
            #     ans+=board[r][c]
            # for dx,dy in direction:
            #     new_x=r+dx
            #     new_y=c+dy
            #     if inbound(new_x,new_y) and (new_x,new_y) not in visited:
            #         dfs(new_x,new_y)


        for i in range(n):
            for j in range(m):
                visited=set()
                if dfs(i,j,0):
                    return True
        return False
        