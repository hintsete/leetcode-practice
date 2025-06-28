class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans=[]
        c1=s[0]
        c2=s[3]
        r1=int(s[1])
        r2=int(s[4])
        print(r1)
        print(r2)
        for col in range(ord(c1),ord(c2)+1):
            for row in range(r1,r2+1):
                ans.append(chr(col)+str(row))
        
        
        

        return ans

      
        
        