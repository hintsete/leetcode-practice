class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # if len(citations)==1 and citations[0]!=0:
        #     return 1
        # elif len(citations)==1 and citations[0]==0:
        #     return 0

        # else:
        #     mid=len(citations)//2
        #     if len(citations)%2==0:
        #         return citations[mid-1]
        #     else:
        #         return citations[mid]
        # ans=0
        # def valid(mid):
        #     count=0
        #     for num in citations:
        #         if mid<=num:
        #             count+=1
        #     return mid<=count
        l=0
        r=len(citations)-1
        while l<=r:
            mid=(l+r)//2
            paper=len(citations)-mid
            if citations[mid]==paper:
                return paper
            elif citations[mid]>paper:
                r=mid-1

            else:
                l=mid+1
          
                
        return len(citations)-l
