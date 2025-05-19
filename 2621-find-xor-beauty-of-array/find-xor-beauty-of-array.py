class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        prefix=0
        for i in range(len(nums)):
            prefix^=nums[i]

        return prefix