class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set=set()
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] not in my_set:
                my_set.add(nums[i]) 
            else:
                nums[i]=float(inf)
        nums.sort()
        return len(nums[:len(my_set)])