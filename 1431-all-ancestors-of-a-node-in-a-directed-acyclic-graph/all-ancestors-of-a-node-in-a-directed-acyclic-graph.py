class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming = defaultdict(int)
        graph = defaultdict(list)
        answer = [set() for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            incoming[v]+=1
        queue = deque()
        for i in range(n):
            if incoming[i]==0:
                queue.append(i)
        while queue:
            node = queue.popleft()
           
            for neigh in graph[node]:
                answer[neigh].add(node)
                answer[neigh].update(answer[node])
                
                incoming[neigh]-=1
                if incoming[neigh]==0:
                    queue.append(neigh)
            
        return [sorted(list(ans)) for ans in answer]
                

       
        
        

        