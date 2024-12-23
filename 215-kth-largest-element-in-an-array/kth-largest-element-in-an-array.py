class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # index of the kth largest element
        nums.sort()
        return nums[len(nums)-k]