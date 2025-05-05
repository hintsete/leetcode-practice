class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n = len(targetGrid)
        m = len(targetGrid[0])
        colors=set()
        bound=defaultdict(list)
        for r in range(n):
            for c in range(m):
                color=targetGrid[r][c]
                colors.add(color)
                if color not in bound:
                    bound[color].append(r)
                    bound[color].append(r)
                    bound[color].append(c)
                    bound[color].append(c)
                else:
                    bound[color][0]=min(bound[color][0], r)
                    bound[color][1]=max(bound[color][1], r)
                    bound[color][2]=min(bound[color][2], c)
                    bound[color][3]=max(bound[color][3], c)
        graph=defaultdict(set)
        incoming=defaultdict(int)
        for col in colors:
            r1,r2,c1,c2=bound[col]
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    other=targetGrid[r][c]
                    if other!=col:
                        if other not in graph[col]:
                            graph[col].add(other)
                            incoming[other]+=1
        queue=deque()
        count=0
        for color in colors:
            if incoming[color]==0:
                queue.append(color)
        while queue:
            color=queue.popleft()
            count+=1
            for neigh in graph[color]:
                incoming[neigh]-=1
                if incoming[neigh]==0:
                    queue.append(neigh)
        return count==len(colors)



