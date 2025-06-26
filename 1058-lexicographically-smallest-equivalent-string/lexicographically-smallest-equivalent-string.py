class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

        parent={i:i for i in range(26)}
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]
        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                if p1<p2:
                    parent[p2]=p1
                else:
                    parent[p1]=p2

        for x,y in zip(s1,s2):
            ord_x=ord(x)-ord("a")
            ord_y=ord(y)-ord("a")
            union(ord_x,ord_y)

        res=[]
        for ch in baseStr:
            val=find(ord(ch)-ord("a"))
            res.append(chr(val+ord("a")))

        return "".join(res)
            

            

        