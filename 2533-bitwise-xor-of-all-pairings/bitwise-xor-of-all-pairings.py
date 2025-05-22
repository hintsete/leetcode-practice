class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        prefix1=0
        prefix2=0
        
        for num in nums1:
            prefix1^=num
        for num in nums2:
            prefix2^=num

        ans=0
        if len(nums1)%2==1:
            ans^=prefix2

        if len(nums2)%2==1:
            ans^=prefix1

        return ans