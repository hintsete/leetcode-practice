class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[-1]*len(nums)
        new_arr=nums+nums
        print(new_arr)
        for i in range(len(new_arr)):
            idx=i%len(nums)
            while stack and nums[idx]>nums[stack[-1]]:
                ans[stack.pop()]=nums[idx]
            stack.append(idx)
        return ans

        