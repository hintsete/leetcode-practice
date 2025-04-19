class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=deque()
        queue.append(0)
        visited=set()
        visited.add(0)
        while queue:
            node= queue.popleft()
            for key in rooms[node]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        return len(visited)==len(rooms)
      
        