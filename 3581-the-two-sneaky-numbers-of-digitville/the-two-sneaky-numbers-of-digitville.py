class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for key,value in count.items():
            if value==2:
                res.append(key)
        return res
        