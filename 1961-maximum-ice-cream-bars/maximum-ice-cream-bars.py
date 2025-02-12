class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        _sum=0
        count=0
        for cost in costs:
            if _sum+cost>coins:
                break
            _sum+=cost
            count+=1
        return count