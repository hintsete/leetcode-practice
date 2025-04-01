class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        curr_force=1
        def valid(mid):
            count=1
            last_pos=position[0]
            for i in range(1,len(position)):
                if position[i]-last_pos>=mid:
                    count+=1
                    last_pos=position[i]
                    if count==m:
                        return True
            return count>=m

            


        l=1
        r=max(position)
        ans=0
        while l<=r:
            mid=(l+r)//2
            if valid(mid):
                ans=mid
                l=mid+1

            else:
                r=mid-1

        return ans
        