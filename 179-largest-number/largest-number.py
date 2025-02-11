class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        print(nums)
        # for i,n in enumerate(nums):
        #     nums[i]=str(n)
        # def comparator(n1,n2):
        #     if n1 + n2>n2 + n1:
        #         return -1
        #     else:
        #         return 1
        # nums=sorted(nums,key=cmp_to_key(compartor))
        # return str(int("".join(nums)))
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]+nums[j+1]<nums[j+1]+nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                
            
        print(nums)

        return str(int("".join(nums)))




            
            