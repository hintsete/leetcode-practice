class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=float(inf)
                cnt+=1

        nums.sort()
        n=len(nums)
        return len(nums[:n-cnt])
