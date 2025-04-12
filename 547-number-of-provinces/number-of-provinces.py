class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        def dfs(node):
            for neigh in range(n):
                if isConnected[node][neigh]==1 and not visited[neigh]:
                    visited[node]=True
                    dfs(neigh)
      

        province=0
        for node in range(n):
            if not visited[node]:
                visited[node]=True
                dfs(node)
                province+=1
            
        return province
