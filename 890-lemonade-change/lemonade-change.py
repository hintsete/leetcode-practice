class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten=0
        five=0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if five>=1:
                    five-=1
                    ten+=1
                else:
                    return False
            elif bill==20:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
              
                else:
                    return False
        return True
       
        # prefix=[0]
        # running_sum=0
        # for bill in bills:
        #     if bill==5:
        #         running_sum+=bill
        #     if bill>5:
        #         running_sum+=(bill-5)
        #     prefix.append(running_sum)
        # print(prefix)
        # # print(0%10)
        # for x,y in zip(prefix,bills):
            
        #     if abs(x-y%10)==5 :
        #         return True
        #     else:
        #         return False
        #     # print(abs(x-y))

        