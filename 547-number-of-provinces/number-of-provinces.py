class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        province=set()
        root={i:i for i in range(n)}
        def find(x):
            if x==root[x]:
                return x

            root[x]=find(root[x])
            return root[x]

        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                root[p1]=p2

           
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    union(i,j)
        
        for i in range(n):
            province.add(find(i))

            

        return len(province)
