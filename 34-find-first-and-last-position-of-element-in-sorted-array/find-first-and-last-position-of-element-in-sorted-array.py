class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # ans=[-1]*2
        # left=0
        # right=len(nums)-1
        # while left<=right:
        #     mid=(left+right)//2
        #     if nums[mid]==target:
        #         ans[0]=mid
        #         print(mid)
        #         # ans[1]=mid+nums.count(target)
        #         break
        #     elif nums[mid]>target:
        #         right=mid-1
        #     elif nums[mid]<target:
        #         left=mid+1
        # return ans
        start=end=-1
        def first_pos(l,r):
            nonlocal start
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                else:
                    if nums[mid]==target:
                        start=mid
                    r=mid-1
            return start
        def last_pos(l,r):
            nonlocal end
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid-1
                else:
                    if nums[mid]==target:
                        end=mid
                    l=mid+1
            return end
        first,last=first_pos(0,len(nums)-1),last_pos(0,len(nums)-1)
        return [first,last]
            



    


       
       

        