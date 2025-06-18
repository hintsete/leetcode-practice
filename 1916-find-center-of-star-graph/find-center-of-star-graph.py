class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        n=len(edges)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        for node in graph:
            if len(graph[node])>=2:
                return node
        