class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(x):
            pref=0
            for num in x:
                pref^=num

            return pref

        total=0
        for mask in range(1<<len(nums)):
            subset=[]
            for i in range(len(nums)):
                if mask& (1<<i):
                    subset.append(nums[i])

            total+=helper(subset)
            print(subset)
       
        return total
        