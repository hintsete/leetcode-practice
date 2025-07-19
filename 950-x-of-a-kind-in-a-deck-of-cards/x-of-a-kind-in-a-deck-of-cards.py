class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count=Counter(deck)
        check=set()
        for val in count.values():
            check.add(val)
        key=[]
        for k in count.keys():
            key.append(k)
        if len(deck)==1:
            return False
        else:
            def compute_gcd(nums):
                return reduce(gcd, nums)
            
            return compute_gcd(check) >= 2 

        