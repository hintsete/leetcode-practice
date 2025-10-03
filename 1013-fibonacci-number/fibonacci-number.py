class Solution:
    def fib(self, n: int, memo=None) -> int:
        prev1=0
        prev2=1
        if n <2:
            return n
        for i in range(2, n+1):
            res= prev1 + prev2
            prev1=prev2
            prev2=res

        return prev2