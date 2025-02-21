class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # output=[0]*(len(adjacentPairs)+1)
        ans=[]
        for i in range(len(adjacentPairs)):
            for j in range(len(adjacentPairs[0])):
                ans.append(adjacentPairs[i][j])
        print(ans)

        count=Counter(ans)
        start=None
        for key,val in count.items():
            if val==1:
                start=key
                break
        # print(output)
        graph=defaultdict(list)
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        
        output=[]
        current=start
        visited=set()
        while len(output)<len(adjacentPairs)+1:
            output.append(current)
            visited.add(current)
            for num in graph[current]:
                if num not in visited:
                    current=num
            # for num in ans:
            #     if num not in visited:
            #         current=num
                    break
        return output

