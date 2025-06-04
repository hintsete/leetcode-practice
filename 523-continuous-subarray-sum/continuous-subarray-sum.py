class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        my_dict={0:-1}
        prefix=0
        for idx,val in enumerate(nums):
            prefix+=val
            mod = prefix%k if k!=0 else prefix

            if mod in my_dict:
                if idx-my_dict[mod] >1:
                    return True

            else:
                my_dict[mod]=idx
        return False
       

        