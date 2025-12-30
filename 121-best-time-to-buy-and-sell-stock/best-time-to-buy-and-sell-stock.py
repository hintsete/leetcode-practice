class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit=prices[j]-prices[i]
        #         max_profit=max(max_profit,profit)

        # if max_profit>0:
        #     return max_profit
        # else:
        #     return 0
        # 7,2,5,3,6,1,4
        n=len(prices)
        # 7:0,1:1,5:2,3:3,6:4,4:5
        min_val=prices[0]
        max_profit=0
        for i in range(n):
            min_val=min(min_val,prices[i])
            max_profit=max(max_profit,prices[i]-min_val)
    

        return max_profit
       
