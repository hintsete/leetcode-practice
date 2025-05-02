class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent={i:i for i in range(1,n+1)}
        rank={i:0 for i in range(1,n+1)}
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return parent[x]
        def union(u,v):
            rootu=find(u)
            rootv=find(v)
            if rootu==rootv:
                return False
            if rootu!=rootv:
                if rank[rootu]>rank[rootv]:
                    parent[rootv]=rootu
                elif rank[rootu]<rank[rootv]:
                    parent[rootu]=rootv
                else:
                    parent[rootv]=rootu
                    rank[rootu]+=1
            return True
            
        for u,v in edges:
            if not union(u,v):
                return [u,v]
           

        