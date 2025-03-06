class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}
        for num in nums2:
            while stack and num>stack[-1]:
                next_greater[stack.pop()]=num
            stack.append(num)
        while stack:
            next_greater[stack.pop()]=-1
        output=[]
        for num in nums1:
            output.append(next_greater.get(num,-1))
        return output
    
