class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        ans = 0
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))

                if grid[i][j] == 1:
                    fresh += 1
        def inbound(r,c):
            return 0 <= r < n and 0 <= c< m
        if fresh == 0:
            return 0
        direction = [(-1 , 0), (1 , 0), (0 , -1), (0 , 1)]

        while queue and fresh >0:
            for _ in range(len(queue)):
                r , c = queue.popleft()

                for x,y in direction:
                    new_r = r + x
                    new_c = c + y
                    if inbound(new_r , new_c) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        queue.append((new_r,new_c))
            if queue:
                ans += 1
        # print(ans)
        return ans if fresh == 0 else -1



                
    