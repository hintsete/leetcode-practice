

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))  
        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1

        return max_len
