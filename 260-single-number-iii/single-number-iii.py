class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        count=Counter(nums)
        for c in count:
            if count[c]==1:
                ans.append(c)

        return ans
        