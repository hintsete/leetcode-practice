class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles)==2:
            return True

        # dp=[False]*len(piles)
        n=len(piles)
        memo={}
        def dp(l,r):
            if l==r:
                return piles[l]
            if (l,r) in memo:
                return memo[(l,r)]
            else:
                memo[(l,r)]=max(piles[l]-dp(l+1,r), piles[r]-dp(l,r-1))

            return memo[(l,r)]

        return dp(0,n-1)>0