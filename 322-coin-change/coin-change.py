class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dp(i,amount):
            if amount==0:
                return 0
            if i>=len(coins) or amount<0:
                return float("inf")
            if (i,amount) in memo:
                return memo[(i,amount)]
            memo[(i,amount)]=min(dp(i+1,amount), 1+dp(i,amount-coins[i]))
            return memo[(i,amount)]
            
        ans=dp(0,amount)
        return ans if ans!= float("inf") else -1
        