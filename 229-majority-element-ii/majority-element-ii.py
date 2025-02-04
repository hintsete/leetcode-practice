class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        n=len(nums)
        for key,value in count.items():
            if value> n/3:
                res.append(key)
            
        return res
        