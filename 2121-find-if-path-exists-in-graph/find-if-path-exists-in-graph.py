class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        seen=defaultdict(list)
        for u,v in edges:
            seen[u].append(v)
            seen[v].append(u)
        
        
        def dfs(node,visited):
            if node==destination:
                return True
            visited.add(node)
            for neigh in seen[node]:
                if neigh not in visited:
                    res=dfs(neigh,visited)
                    if res==True:
                        return True
            return False
        return dfs(source,set())

            
     