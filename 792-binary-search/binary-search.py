class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l=0
        # r=len(nums)-1
        # mid=(l+r)//2
        # if nums[mid]==target:
        #     return mid
        # elif nums[mid]>target:
        #     r=mid-1
        # elif nums[mid]<target:
        #     l=mid+1
        



        def solve(l,r,nums,target):
            if l>r:
                return -1
                

            
            
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            
            

            elif nums[mid]>target:
                
                return solve(l,mid-1,nums,target)

            elif nums[mid]<target:
                return solve(mid+1,r,nums,target)
         
        return solve(0,len(nums)-1,nums,target)
            


        