class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        filtered=set()
        for u,v in edges:
            filtered.add(v)
        players=set(range(n))
        winners=players-filtered
        if len(winners)==1:
            return winners.pop()
        return -1
      

         