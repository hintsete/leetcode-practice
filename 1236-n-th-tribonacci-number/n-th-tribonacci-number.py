class Solution:
    def tribonacci(self, n: int,memo=None) -> int:
        # memo={}
        if memo==None:
            memo={0:0,1:1,2:1}
        if n in memo:
            return memo[n]

        memo[n]=self.tribonacci(n-1,memo)+self.tribonacci(n-2,memo)+self.tribonacci(n-3,memo)
        return memo[n]

