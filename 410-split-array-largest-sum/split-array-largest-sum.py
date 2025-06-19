class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=max(nums)
        r=sum(nums)
        ans=r
        def valid(mid):
            count=1
            curr_sum=0
            for num in nums:
                if curr_sum+num>mid:
                    count+=1
                    curr_sum=num
                else:
                    curr_sum+=num

            return count<=k

        while l<=r:
            mid=(l+r)//2
            if valid(mid):
                ans=mid
                r=mid-1
                

            else:
                l=mid+1
                

        return ans

        
        