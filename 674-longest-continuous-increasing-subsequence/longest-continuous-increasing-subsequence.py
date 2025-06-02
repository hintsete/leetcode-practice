class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l=0
        max_len=0
        window=[]
        for r in range(len(nums)):
            if not window or window[-1]<nums[r]:
                window.append(nums[r])

            else :
                window=[nums[r]]

                

            max_len=max(max_len,len(window))
        return max_len

        