class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=1
        def valid(mid):
            total_sum=0
            for pile in piles:
                total_sum+=ceil(pile/mid)
            return total_sum<=h

        while low<=high:
            mid=(low+high)//2
            if valid(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

                
