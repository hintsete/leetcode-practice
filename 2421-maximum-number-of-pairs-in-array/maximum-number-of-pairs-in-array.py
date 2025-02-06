class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        n=len(nums)
        c=0
        for val in count.values():
            if val>1:
                p=val//2
                c+=p
        return [c,n-(2*c)]
        