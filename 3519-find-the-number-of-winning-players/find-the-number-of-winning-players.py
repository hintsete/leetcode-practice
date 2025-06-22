class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        pick.sort(key=lambda x:x[0])
        p=defaultdict(list)
        for start,end in pick:
            p[start].append(end)
        print(p)
        ans=0
        for key,val in p.items():
            count=Counter(val)
            if key<max(count.values()):
                ans+=1

        return ans


        






















        


        
        


        