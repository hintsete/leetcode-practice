class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        a={"(":")","[":"]","{":"}"}
        for char in s:
            if char in a:
                stack.append(char)
            elif char in a.values():
                if not stack or a[stack.pop()]!=char:
                    return False
                
            
        return len(stack)==0
