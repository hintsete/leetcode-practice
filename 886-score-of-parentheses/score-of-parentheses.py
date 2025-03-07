class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        
        for ch in s:
            if ch=="(":
                stack.append(0)
            else:
                val=stack.pop()
                if val==0:
                    score=1
                else:
                    score=val*2
                if stack:
                    stack[-1]+=score
                else:
                    stack.append(score)
             
        return stack[0]
