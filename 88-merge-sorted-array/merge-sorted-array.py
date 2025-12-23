class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=len(nums1)
        i=0
        while i<n and m<x:
            nums1[m]=nums2[i]
            i+=1
            m+=1
        nums1.sort()
        