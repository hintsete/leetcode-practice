class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero=0
        product=1
        def factorial(n):
            if n==1 or n==0:
                return 1
            prev=factorial(n-1)
            curr=n*prev
            return curr
        def trailingZero(number):
            if number%10!=0:
                return 0
            return 1+trailingZero(number//10)
        fact_n=factorial(n)
        ans=trailingZero(fact_n)
        return ans
    
            


       



        