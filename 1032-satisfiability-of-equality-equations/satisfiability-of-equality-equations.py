class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph={}
        def find(x):
            if x!=graph[x]:
                graph[x]=find(graph[x])
            return graph[x]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            graph[rootx]=rooty
      
        for s in equations:
            x=s[0]
            y=s[3]
            if x not in graph:
                graph[x]=x
            if y not in graph:
                graph[y]=y
        for s in equations:
            if s[1]=="=":
                union(s[0],s[3])
        for s in equations:
            if s[1]=="!":
                rootx=find(s[0])
                rooty=find(s[3])
                if rootx==rooty:
                    return False
        return True

            
      
        