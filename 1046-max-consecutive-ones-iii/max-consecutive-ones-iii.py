class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len=0
        left=0
        zero_count=0
        for right in range(len(nums)):
            # max_len=max(max_len,right-left+1)
            # while binary.count(0)==k:
            #     binary.remove(nums[left])
            #     left+=1

            # binary.append(nums[right])
            if nums[right]==0:
                zero_count+=1
            while zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1

            max_len=max(max_len,right-left+1)


                

        return max_len
        