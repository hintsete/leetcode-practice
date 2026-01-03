class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #no papers h
        #cited h times
        #no of papers with highest citation
        n=len(citations)
        h=0
        citations.sort(reverse=True)
        for i in range(n):
            if i+1<=citations[i]:
                h+=1
        return h
      

        