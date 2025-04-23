class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        order = []
        incoming = [0 for _ in range(len(graph))]
        reverse_graph = defaultdict(list)
        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)
                incoming[i]+=1
        
        queue = deque()
        for i in range(len(graph)):
            if incoming[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            order.append(node)
            for neigh in reverse_graph[node]:
                incoming[neigh] -= 1
                if incoming[neigh]==0:
                    queue.append(neigh)
        return sorted(order)
        