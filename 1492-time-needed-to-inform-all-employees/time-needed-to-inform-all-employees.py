class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=defaultdict(list)
        total=0
        visited=set()
        for i in range(n):
            graph[manager[i]].append(i)

        def dfs(node):
            total=0
            for neigh in graph[node]:
                total=max(total,dfs(neigh))

            return informTime[node]+total
        return dfs(headID)
            # total=0
            # visited.add(node)
            # total+=informTime[node]
            # return total


        # for key,val in graph.items():
        #     if key==-1:
        #         total+=dfs(key)
                
        #         for neigh in graph[key]:
        #             if neigh not in visited:
        #                 total+=dfs(neigh)
            
        # return total


        print(graph)
        # for key,val in graph.items():
        #     if graph[key]==-1:
        #         visited.add(key)
        #         total+=informTime [key]
        #         for neigh


        