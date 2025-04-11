class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color = [-1 for _ in range(n)]
        result = True
        def dfs(node):
            temp = True
            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[node] 
                    temp = temp and dfs(neigh)

                elif color[neigh] == color[node]:
                    return False
            return temp
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                result = result and dfs(node)
        return result

            
        