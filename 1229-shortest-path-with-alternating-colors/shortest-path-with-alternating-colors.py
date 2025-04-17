class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)
        for u,v in redEdges:
            red[u].append(v)
        for u,v in blueEdges:
            blue[u].append(v)
        queue=deque()
        visited=set()
        queue.append((0,0,0))
        queue.append((0,1,0))
        visited.add((0,0))
        visited.add((0,1))
        res=[-1]*n
        res[0]=0
        while queue:
            node,color,length = queue.popleft()
            if res[node] == -1:
                res[node]=length
            else:
                res[node] = min(res[node],length)

            next_color = 1 - color
            next_edge = blue[node] if next_color == 1 else red[node]
            for neigh in next_edge:
                if (neigh,next_color) not in visited:
                    visited.add((neigh,next_color))
                    queue.append((neigh,next_color,length+1))
            
        return res

        
