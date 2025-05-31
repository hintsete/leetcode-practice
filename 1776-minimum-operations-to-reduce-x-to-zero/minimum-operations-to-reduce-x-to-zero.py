class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)-x
        if total<0:
            return -1
        curr_sum=0
        l=0
        max_len=-1
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while curr_sum>total and l<=r:
                curr_sum-=nums[l]
                l+=1
            if curr_sum==total:
                max_len=max(max_len,r-l+1)

        return len(nums)-max_len if max_len!=-1 else -1

        
        