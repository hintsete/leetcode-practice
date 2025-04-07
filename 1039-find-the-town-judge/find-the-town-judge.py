class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count=defaultdict(int)
        trusted=defaultdict(int)
        for u,v in trust:
            trust_count[u]+=1
            trusted[v]+=1
        for i in range(1,n+1):
            if trust_count[i]==0 and trusted[i]==n-1:
                return i
        return -1


       



    
    
       