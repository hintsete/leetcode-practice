class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for n in num:
            while k>0 and stack and stack[-1]>n:
                stack.pop()
                k-=1

            stack.append(n)

        if k>0:
            stack=stack[:-k]

        ans="".join(stack).lstrip('0')
        return ans if ans else "0"
        
        

        