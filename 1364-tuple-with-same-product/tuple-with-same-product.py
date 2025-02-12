class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product=defaultdict(int)
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product[nums[i]*nums[j]]+=1

        for val in product.values():
            if val>1:
             res+=(val*(val-1)//2)*8
        return res

        