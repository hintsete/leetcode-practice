class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        one=self.fib(n-1)
        two=self.fib(n-2)
        return one+two

        