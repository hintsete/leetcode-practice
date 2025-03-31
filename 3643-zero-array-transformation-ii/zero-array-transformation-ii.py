class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def valid(mid):

            diff_array=[0]*(len(nums)+1)
            for i in range(mid):
                l,r,val=queries[i]
                diff_array[l]-=val
                if r+1<len(diff_array):
                    diff_array[r+1]+=val
            # for i in range(1,)
            current=0
            for i in range(len(nums)):
                current+=diff_array[i]
                if current+nums[i]>0:
                    return False
            return True
        l=0
        r=len(queries)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if valid(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans