class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(mid):
            total=0
            for c in candies:
                total+=(c//mid)
            return total>=k

        l=1
        r=sum(candies)
        while l<=r:
            mid=(l+r)//2
            if valid(mid):
                l=mid+1
            else:
                r=mid-1
        return r
        