class Solution:
    def romanToInt(self, s: str) -> int:
        num=[1,5,10,50,100,500,1000]
        char=["I","V","X","L","C","D","M"]
        my_dict=dict(zip(char,num))
        total=0
        index=0
        while index < len(s):
            if index+1< len(s) and my_dict[s[index]]<my_dict[s[index+1]]:
                total+=my_dict[s[index+1]]-my_dict[s[index]]
                index+=2
            else:
                total+=my_dict[s[index]]
                index+=1
            
        return total

        