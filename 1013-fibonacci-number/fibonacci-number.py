class Solution:
    def fib(self, n: int, memo=None) -> int:
        if memo==None:
            memo={0:0,1:1}
        if n in memo:
            return memo[n]
        memo[n]=self.fib(n-1,memo)+self.fib(n-2,memo)
        return memo[n]
        