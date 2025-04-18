class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        if image[sr][sc]==color:
            return image
        queue = deque()
        initial = image[sr][sc]
        visited = set()
        queue.append((sr,sc))
        visited.add((sr,sc))
        image[sr][sc]=color
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        while queue:
            r,c = queue.popleft()
            for x,y in direction:
                new_r=r+x
                new_c=c+y
                if inbound(new_r,new_c) and image[new_r][new_c]==initial and (new_r,new_c) not in visited:
                    image[new_r][new_c]=color
                    visited.add((new_r,new_c))
                    queue.append((new_r,new_c))
        return image
                    
        