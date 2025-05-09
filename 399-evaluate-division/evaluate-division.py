class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(dict)
        for idx,ls in enumerate(equations):
            x,y=ls
            graph[x][y]=values[idx]
            graph[y][x]=1/values[idx]
        print(graph)
        
        def bfs(src,des):
            visited=set()
            queue=deque()
            queue.append((src,1.0))
            visited.add(src)
            if src not in graph or des not in graph:
                return -1.0
            if src==des:
                return 1
            while queue:
                node,w=queue.popleft()
                if node==des:
                    return w
                for neigh,curr_val in graph[node].items():
                    if neigh not in visited:
                        queue.append((neigh,w*curr_val))
                        visited.add(neigh)
            return -1
        return [ bfs(u,v) for u,v in queries]

            
            


        