class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        composite=max(candies)-extraCandies
        res=[]
        for num in candies:
            if num>=composite:
                res.append(True)

            else:
                res.append(False)

        return res
        