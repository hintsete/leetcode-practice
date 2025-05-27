class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1!=p2:
                parent[p2]=p1
            
                # parent[p2]=p1


        parent={i:i for i in range(len(source))}
        # parent={}

        for u,v in allowedSwaps:
            union(u,v)
        component=defaultdict(list)
        for i in range(len(source)):
            root=find(i)
            component[root].append(i)
        dist=0
        for val in component.values():
            c1=Counter(source[i] for i in val)
            c2=Counter(target[i] for i in val)
            for key in c2:
                count=c2[key]-c1.get(key,0)
                if count>0:
                    dist+=count

        return dist


            
                



            


       

            
            


        

