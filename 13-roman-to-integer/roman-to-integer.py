class Solution:
    def romanToInt(self, s: str) -> int:
        # num//roman=val=remainder
        # the remainder should be less than the value
        # num%roman<num but max 

        my_dict={
            "I" :1,
            "V" :5,
            "X" :10,
            "L" :50,
            "C" :100,
            "D" :500,
            "M" :1000,
        }
        cnt=0
      
        for i in range(len(s)-1):
            if my_dict[s[i]]<my_dict[s[i+1]]:
                cnt-=my_dict[s[i]]
            elif my_dict[s[i]]>=my_dict[s[i+1]]:
                cnt+=my_dict[s[i]]
        cnt+=my_dict[s[-1]]
       
            # cnt+=my_dict[s[i]]
        # cnt+=my_dict[s[-1]]
            
        
          
        return cnt



           