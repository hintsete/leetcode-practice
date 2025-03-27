class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        ans=right
        def valid(mid):
            total_weight=0
            ship_day=1
            for weight in weights:
                if total_weight+weight>mid:
                    ship_day+=1
                    total_weight=0
                total_weight+=weight
            
            return ship_day<=days
            #validate answer
        while left<=right:
            mid=(left+right)//2
            if valid(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
    

        
        