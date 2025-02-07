class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # nums_left=[]
        # output=[]
        # count_one=0
        # for num in nums:
        #     if num==1:
        #         count_one+=1
        # i=0
        # _max=-1
        # while i <len(nums):
        #     idx_sum=nums_left.count(0)+count_one-nums_left.count(1)
        #     if idx_sum>_max:
        #         output=[i]
        #         _max=max(_max,idx_sum)
        #     elif idx_sum==_max:
        #         output.append(i)
            
        #     # output.append(i)
        #     nums_left.append(nums[i])
        #     i+=1
        # return output
        zero_count=nums.count(0)
        one_count=nums.count(1)
        zero_left=0
        one_left=0
        output=[]
        _max=-1
        for i in range(len(nums)+1):
            zero_right=zero_count-zero_left
            one_right=one_count-one_left

            idx_sum=zero_left+one_right
            if idx_sum>_max:
                _max=idx_sum
                output=[i]
            elif idx_sum==_max:
                output.append(i)
            if i <len(nums):
                if nums[i]==0:
                    zero_left+=1
                else:
                    one_left+=1
        return output




        