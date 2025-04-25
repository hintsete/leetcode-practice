class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        min_heights = defaultdict(int)
        queue = deque()
        # anscetor = [set() for _ in range(n)]
        for root,val in graph.items():
            if len(val)==1:
                queue.append(root)
            min_heights[root] = len(val)
        while queue:
            if n<=2:
                return list(queue)
            
            curr_len = len(queue)
            for i in range(curr_len):
                node = queue.popleft()
                n-=1
                for neigh in graph[node]:
                    min_heights[neigh] -= 1
                    if min_heights[neigh]== 1:
                        queue.append(neigh)



            
   


