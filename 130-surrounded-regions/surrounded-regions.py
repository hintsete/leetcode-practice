class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
       
        def dfs(r,c):
            if r<0 or r >=n or c<0 or c>=m or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dx,dy in direction:
                new_x = r+dx
                new_y = c+dy
                dfs(new_x,new_y)
        for i in range(n):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][m-1] == "O":
                dfs(i,m-1)
        for j in range(m):
            if board[0][j] == "O":
                dfs(0,j)
            if board[n-1][j] == "O":
                dfs(n-1,j)

           

                
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j]= "X"
                elif board[i][j] == "T":
                    board[i][j]= "O"