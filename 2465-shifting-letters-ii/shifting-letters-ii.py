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
        #calculate the prefix sum and store it in range_Sum    
        for i in range(1,len(range_Sum)):
            range_Sum[i]+=range_Sum[i-1]
        # to find the number of shift to each char in s
        shifted_chars=[]
        for i in range(len(s)):
            shift=range_Sum[i]%26
            # after computing the shifted postion add ord(a) to map back to lower case letter
            shifted_chars.append(chr((ord(s[i])-ord('a')+shift)%26 + ord('a')))
            
        return "".join(shifted_chars[:len(s)])

        
    
    
    

