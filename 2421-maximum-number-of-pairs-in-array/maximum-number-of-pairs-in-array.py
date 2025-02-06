class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        n=len(nums)
        c=0
        for val in count.values():
            while val>1:
                val-=2
                c+=1
        return [c,n-(2*c)]
        