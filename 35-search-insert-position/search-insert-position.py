class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target not in nums:
            nums.append(target)
            nums.sort()

            return nums.index(target)
            nums.remove(target)
        
        