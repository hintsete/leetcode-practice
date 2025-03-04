class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l=0
        ans=0
        for ch in s:
            if ch=="L":
                count_l+=1
            else:
                count_l-=1
            if count_l==0:
                ans+=1
            
        return ans
        