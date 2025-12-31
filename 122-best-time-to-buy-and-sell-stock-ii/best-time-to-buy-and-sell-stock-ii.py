class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        n=len(prices)
        diff=[]
        for i in range(n-1):
            diff.append(prices[i+1]-prices[i])
        for num in diff:
            if num>=0:
                max_profit+=num
        if max_profit>0:
            return max_profit
        else:
            return 0
        #for i in range(n):
        # min_val=prices[n-1]

        # return max_profit
        print(diff)