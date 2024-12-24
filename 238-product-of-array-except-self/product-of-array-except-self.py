class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # set up left and right multiplier to 1 to take care of edge cases
        left_mul=1
        right_mul=1
        size=len(nums)
        # create a left and right array to actually find the product of an element except itself
        left_arr=[0]*size
        right_arr=[0]*size

        for i in range(size):
            j=-1-i
            left_arr[i]=left_mul
            right_arr[j]=right_mul
            left_mul*=nums[i]
            right_mul*=nums[j]
        return [l*r for l,r in zip(left_arr,right_arr)]
        
            
