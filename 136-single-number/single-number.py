class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        # for item in nums:
        #     if nums.count(item)==1:
        #         return item
        prefix=nums[0]
        for num in nums[1:]:
            prefix^=num

        return prefix
            

       
            