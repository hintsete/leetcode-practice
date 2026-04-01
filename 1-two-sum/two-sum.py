class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in diff:
                return [i,diff[compl]]
            diff[nums[i]]=i