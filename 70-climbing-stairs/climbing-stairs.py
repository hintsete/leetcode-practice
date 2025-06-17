class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def helper(x):
            if x==1:
                return 1

            elif x==2:
                return 2

            # return helper(x-1)+helper(x-2)
            if x in memo:
                return memo[x]

            memo[x]=helper(x-1)+helper(x-2)
            return memo[x]

        return helper(n)
        