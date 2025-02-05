class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count=Counter(nums)
        # res=[]
        # n=len(nums)
        # for key,value in count.items():
        #     if value> n/2:
        #         res.append(key)
            
        # return max(res)
        res=0
        count=0
        for num in nums:
            if count==0:
                res=num
            count+=1 if res==num else -1
           



        return res

        