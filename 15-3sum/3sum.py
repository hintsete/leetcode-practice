class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i=0
        # j=i+1
        # k=i+2
        # # curr_sum=
        # output=[]
        # while k<len(nums):
        #     curr_sum=nums[i]+nums[j]+nums[k]
        #     if curr_sum==0:
        #         output.extend((nums[i],nums[j],nums[k]))
        #         i+=1
        #         j+=1
        #         k+=1
        i=0
        output=set()
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                curr_sum=nums[i]+nums[l]+nums[r]
                if curr_sum==0:
                    if (nums[i],nums[l],nums[r]) not in output:
                     output.add((nums[i],nums[l],nums[r]))
                    # i+=1
                    l+=1
                    r-=1
                elif curr_sum<0:
                    l+=1
                elif curr_sum>0:
                    r-=1
                else:
                    l+=1
                    r-=1
                    i+=1
        return list(output)


        