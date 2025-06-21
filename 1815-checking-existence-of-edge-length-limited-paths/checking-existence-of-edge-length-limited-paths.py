class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        parent={i:i for i in range(n)}
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                parent[p2]=p1

        edgeList.sort(key=lambda x:x[2])
        query=[(u,v,w,idx) for idx, (u,v,w) in enumerate(queries)]
        ans=[False]*len(queries)
        query.sort(key=lambda x:x[2])
        i=0
        for u,v,w,idx in query:
            while i<len(edgeList) and edgeList[i][2]<w:
                union(edgeList[i][0],edgeList[i][1])
                i+=1

            ans[idx]= find(u)==find(v)

        return ans
        