class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        l=0
        r=0
        while r< (len(nums)-1):
            curr_distance=0
            for i in range(l,r+1):
                curr_distance=max(curr_distance, i+nums[i])
            l=r+1
            r=curr_distance
            jump+=1
        return jump
        