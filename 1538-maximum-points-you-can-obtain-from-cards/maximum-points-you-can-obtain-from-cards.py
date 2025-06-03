class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints[:k])
       
        max_total=total
        l=k-1
        r=len(cardPoints)-1
        while l>=0:
            total-=cardPoints[l]
            total+=cardPoints[r]
            max_total=max(max_total,total)
            l-=1
            r-=1
        return max_total
