class DSU:
    def __init__(self,n):
        self.n=n
        self.root={i:i for i in range(1,n+1)}
        self.size={i:1 for i in range(1,n+1)}

    def find(self,x):
        if self.root[x]!=x:
            self.root[x]=self.find(self.root[x])

        return self.root[x]


    def union(self,x,y):
        p1=self.find(x)
        p2=self.find(y)
        if p1==p2:
            return 0
        if self.size[p1]>=self.size[p2]:
            self.root[p2]=p1
            self.size[p1]+=self.size[p2]
        else:
            self.root[p1]=p2
            self.size[p2]+=self.size[p1]
        self.n-=1
        return 1

        

    def is_connected(self):
        return self.n==1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        count=0
        alice=DSU(n)
        bob=DSU(n)
        for ty,a,b in edges:
            if ty==3:
                x=bob.union(a,b)
                y=alice.union(a,b)
                if x or y:
                    count+=1
        for ty,a,b in edges:
            if ty==1:
                if alice.union(a,b):
              
                    count+=1
            elif ty==2:
                if bob.union(a,b):
                    count+=1

        if alice.is_connected() and bob.is_connected():
            return len(edges)-count
        

            
        return -1

        

        