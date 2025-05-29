class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        to_s={}
        to_t={}
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if c1 in to_t:
                if to_t[c1]!=c2:
                    return False

            else:
                to_t[c1]=c2

            if c2 in to_s:
                if to_s[c2] !=c1:
                    return False

            else:
                to_s[c2]=c1
        return True
        