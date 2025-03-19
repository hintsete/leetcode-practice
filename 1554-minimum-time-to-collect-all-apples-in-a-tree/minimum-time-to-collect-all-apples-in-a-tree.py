class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacency_list={i:[] for i in range(n)}
        for u,v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        def dfs(curr,par):
            time=0
            for neighbor in adjacency_list[curr]:
                if neighbor==par:
                    continue
                child_time=dfs(neighbor,curr)
                if child_time>0 or hasApple[neighbor]:
                    time+=2+child_time
            return time
        return dfs(0,-1)
            
        