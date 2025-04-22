class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r ,c =click
        n= len(board)
        m= len(board[0])
        print(r)
        print(c)
        if board[r][c]=="M":
            board[r][c]="X"
            return board
        queue = deque()
        visited = set()
        queue.append((r,c))
        # visited.add((r,c))
        direction = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
        def helper(x,y):
            count=0
            for dx,dy in direction:
                new_x=dx+x
                new_y=dy+y
                if inbound(new_x,new_y) and (new_x,new_y) not in visited and board[new_x][new_y]=="M":
                    count+=1
            return count

        
        while queue:
            x,y=queue.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if board[x][y]=="E":
                val=helper(x,y)
                if val == 0:
                    board[x][y]="B"
                    for dx,dy in direction:
                        new_x=dx+x
                        new_y=dy+y
                        if inbound(new_x,new_y) and (new_x,new_y) not in visited:
                            queue.append((new_x,new_y))
                            
                else:
                    board[x][y]=str(val)

            
        return board



        