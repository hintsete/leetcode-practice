class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        range_Sum=[0]*(len(s)+1)

        for start,end,direction in shifts:
            if direction==1:
                range_Sum[start]+=1
                if end+1<len(range_Sum):
                    range_Sum[end+1]-=1
                
            else:
                range_Sum[start]-=1
                if end+1 < len(range_Sum):
                    range_Sum[end+1]+=1
         
        for i in range(1,len(range_Sum)):
            range_Sum[i]+=range_Sum[i-1]
        
        shifted_chars=[]
        for i in range(len(s)):
            shift=range_Sum[i]%26
            new_val=ord(s[i])+shift
            if new_val>122:
                new_val-=26
            if new_val<97:
                new_val+=26
            shifted_chars.append(chr(new_val))
        return "".join(shifted_chars)

        #     # after computing the shifted postion add ord(a) to map back to lower case letter
        #     shifted_chars.append(chr((ord(s[i])-ord('a')+shift)%26 + ord('a')))
        # # print(ord("h")-ord("a"))
            
        # return "".join(shifted_chars[:])

        
    
    
    

