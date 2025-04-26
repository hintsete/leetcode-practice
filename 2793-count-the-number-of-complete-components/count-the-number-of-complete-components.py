class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0
        def dfs(node,path):
            nonlocal count
            if node in visited:
                return 
            visited.add(node)
            path.append(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh,path)
        for i in range(n):
            if i not in visited:
                path = []
                dfs(i,path)
                complete=True
                for node in path:
                    if len(graph[node])!=len(path)-1:
                        complete=False
                        break
                if complete:
                    count+=1
            
        


      
            
        return count


        