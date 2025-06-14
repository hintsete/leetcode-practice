class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_cnt=0
        l=0
        n=len(nums)
        window=[]
        max_len=0
        for r in range(n):
            if nums[r]==0:
                zero_cnt+=1

            while zero_cnt>1:
                if nums[l]==0:
                    zero_cnt-=1

                l+=1

            max_len=max(max_len,r-l)
               

        return max_len



        