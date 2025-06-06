class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res=[]
        incoming=[0]*numCourses
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
            incoming[v]+=1

        pre=[set() for _ in range(numCourses)]
        queue=deque()
        for i in range(numCourses):
            if incoming[i]==0:
                queue.append(i)

        while queue:
            u=queue.popleft()
            for node in graph[u]:
                pre[node].update(pre[u])
                pre[node].add(u)

                incoming[node]-=1
                if incoming[node]==0:
                    queue.append(node)

        for u,v in queries:
            res.append(u in pre[v])
        return res


        
      