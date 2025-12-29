class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #k%len(nums)
        # nums[:k] + nums[k:]
        n=len(nums)
        k=k%n
        j=n-k
        # print(j)
        # print(nums[j])
        # print(nums[:j])
        # print(nums[j:])
        nums[:k],nums[k:]=nums[j:],nums[:j]
        # nums[:j], nums[j:]=nums[j:],nums[:j]
        