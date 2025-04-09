class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=defaultdict(list)
        # indegree=defaultdict(int)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            # indegree[course]+=1
        white=1
        grey=2
        black=3
        color={course: white for course in range(numCourses)}
        no_cycle=True
        def dfs(node):

            nonlocal no_cycle
            if not no_cycle:
                return
            color[node]=grey
            if node in adj_list:
                for neigh in adj_list[node]:
                    if color[neigh]==white:
                        dfs(neigh)
                    elif color[neigh]==grey:
                        no_cycle=False
                        
            color[node]=black
        for course in range(numCourses):
            if color[course]==white:
                dfs(course)
        return no_cycle