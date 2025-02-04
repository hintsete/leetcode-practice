class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=[]
        n=len(nums)
        for key,value in count.items():
            if value> n/2:
                res.append(key)
            
        return max(res)

        