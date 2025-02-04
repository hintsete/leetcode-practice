class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1=Counter(s)
        count2=Counter(t)

        ans=0
        for key in count2:
            if key not in count1:
                ans+=count2[key]
            elif key in count1 and count2[key]>count1[key]:
                ans+=abs(count1[key]-count2[key]) 
            
        return ans
        
    


        
