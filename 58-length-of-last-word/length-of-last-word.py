class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_str=""
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and last_str=="":
                continue
            elif s[i]==" ":
                break
            last_str+=s[i]
            
            
        return len(last_str)
            
        