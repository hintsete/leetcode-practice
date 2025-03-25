class Solution:
    def mySqrt(self, x: int) -> int:
        sqr=0
        low=0
        high=ceil(x/2)
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=x:
                sqr=mid
                low=mid+1
            else:
                high=mid-1
        return sqr

        