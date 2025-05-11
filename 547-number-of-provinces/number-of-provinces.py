class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent={i:i for i in range(n)}
        rank={i:1 for i in range(n)}
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
                

            return parent[x]
        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                if rank[p1]>rank[p2]:
                    parent[p2]=p1
                elif rank[p1]<rank[p2]:
                    parent[p1]=p2
                else:
                    parent[p2]=p1
                    rank[p1]+=1
        connected=n
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] and find(i)!=find(j):
                    connected-=1
                    union(i,j)
                    
        return connected
       

        # visited=[False]*n
        # def dfs(node):
        #     for neigh in range(n):
        #         if isConnected[node][neigh]==1 and not visited[neigh]:
        #             visited[node]=True
        #             dfs(neigh)
      

        # province=0
        # for node in range(n):
        #     if not visited[node]:
        #         visited[node]=True
        #         dfs(node)
        #         province+=1
            
        # return province
