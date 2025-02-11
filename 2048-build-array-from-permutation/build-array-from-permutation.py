class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        # print(ans)
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        return ans


        