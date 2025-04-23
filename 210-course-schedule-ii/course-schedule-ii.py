class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = defaultdict(list)
        queue = deque()
        incoming = [0 for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            order.append(course)
            for neigh in graph[course]:
                incoming[neigh] -=1

                if incoming[neigh] ==0:
                    queue.append(neigh)
        


        
        return order if len(order) == numCourses else []
        