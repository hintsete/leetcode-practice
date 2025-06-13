class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent={i:i for i in range(1,n+1)}
        print(parent)
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                parent[p2]=p1

        min_val=float(inf)
        for start,end,dist in roads:
            union(start,end)

        for start,end,dist in roads:
            if find(start)==find(1):
                min_val=min(min_val,dist)
                if min_val==1:
                    return 1

        return min_val
               


       