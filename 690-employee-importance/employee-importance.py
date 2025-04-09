"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list=defaultdict(list)
        importance=defaultdict(int)
        for i in employees:
            adj_list[i.id].extend(i.subordinates)
            importance[i.id]=i.importance
        def dfs(node,total,visited):
            if node in visited:
                return 0
            visited.add(node)
            total=importance[node]
            for neigh in adj_list[node]:
                if neigh not in visited:
                    total+=dfs(neigh,total,visited)
            return total
        return dfs(id,0,set())


