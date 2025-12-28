class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=Counter(nums)
        for num in nums:
            if count[num]> n/2:
                return num
        