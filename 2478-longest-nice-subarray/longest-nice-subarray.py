class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len=0
        set_bits=0
        l=0
        for r in range(len(nums)):
            while (set_bits& nums[r])!=0:
                set_bits^=nums[l]
                l+=1

            set_bits|=nums[r]
            max_len=max(max_len,(r-l)+1)
        return max_len

            

           