class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        prefix=[1]
        suffix=[1]
        for i in range(len(nums)-1,-1,-1):
            res=suffix[-1]*nums[i]
            suffix.append(res)
        for num in nums:
            res=prefix[-1]*num
            prefix.append(res)
        suffix=suffix[::-1]
        print(prefix)
        print(suffix)
        for i in range(1,len(prefix)):
            res=prefix[i-1]*suffix[i]
            ans.append(res)
        print(ans)
        return ans

       
        