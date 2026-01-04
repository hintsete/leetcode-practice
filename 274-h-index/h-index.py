class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #no papers h
        #cited h times
        #no of papers with highest citation
        n=len(citations)
        h=0
        citations.sort()
        l=0  
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if citations[mid]>=n-mid:
                print(mid)
                h=n-mid
                
                r=mid-1
            else:
                l=mid+1
        return h

      

        