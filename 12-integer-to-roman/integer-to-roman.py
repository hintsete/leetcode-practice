class Solution:
    def intToRoman(self, num: int) -> str:

        roman={
             1000 : "M",
             900: "CM",
             500 : "D",
             400:"CD",
             100 : "C",
             90:"XC",
             50 : "L",
             40: "XL",
             10 : "X",
             9:"IX",
             5 :  "V",
             4: "IV",
             1 : "I",

        }
        res=""
        for value in roman.keys():
            while num >=value:
                res+=roman[value]
                num-=value
            
        return res
            
            
            
        # my_val=[]
        # for value in roman.keys():
        #     my_val.append(value)
        # sorted(my_val,reverse=True)
        # i=0
        # while i<len(my_val):
        #     while num> my_val[i]:
        #         res+=roman[my_val[i]]
        #         num-my_val[i]
            
        #     i+=1

        # for value in roman.keys():
        #     if num> value:
        #         res+=roman[value]
        
            
        #     value-num

       
        # return res
            




           

      