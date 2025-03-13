class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch!="]":
                stack.append(ch)
            else:
                new_str=""
                while stack[-1]!="[":
                    new_str=stack.pop()+new_str
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(new_str*int(num))
        return "".join(stack)
                    

      
       
        