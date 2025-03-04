class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count=Counter(answers)
        ans=[]
        for key,val in count.items():
            if key==0 :
                ans.append(val)
            else:
                group=(key+val)//(key+1)
                ans.append(group*(key+1))
        # print(ans)
        
        return sum(ans)