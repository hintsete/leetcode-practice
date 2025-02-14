class Solution:
    def minimumSteps(self, s: str) -> int:
        # right=len(s)-1
        count=0
        ans=0
        for right in range(len(s)-1,-1,-1):
            if s[right]=="1":
                count+=ans
            else:
                ans+=1

        return count

    

        # return count

        # zero_counter={}
        # ans=len(s)+1
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]==0:
        #         zero_counter[s[i]]+=1
        #     elif s[i]==1:
        #         ans+=s.get(s[0],0)

        # return ans
        # zero_idx=[]
        # for i in range(len(s)):
        #     if s[i]=="0":
        #         zero_idx.append(i)

