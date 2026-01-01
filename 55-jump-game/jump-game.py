class Solution:
    def canJump(self, nums: List[int]) -> bool:      
        pos=0
        for num in nums:
            if pos<0:
                return False
            elif num > pos:
                pos=num
            pos-=1
        return True
        
        