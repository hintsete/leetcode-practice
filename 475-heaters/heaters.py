class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
       
        max_val=0
        for house in houses:
            l=0
            r=len(heaters)
            while l<r:
                mid=(l+r)//2
                
                if heaters[mid]<=house:
                    l=mid+1

                else:
                    r=mid
            min_distance=float("inf")
            if l<len(heaters):
                min_distance=abs(house-heaters[l])

            if l>0:
                min_distance=min(min_distance,abs(house-heaters[l-1]))
            max_val=max(max_val,min_distance)
        
        return max_val

        # radius = [[0]*len(heaters) for _ in range(len(houses))]

        # for i in range(len(houses)):
        #     for j in range(len (radius[0])):
        #         radius[i][j] = abs(houses[i] - heaters[j])
        # print(radius)
        # ans=[]
        # for i in range(len(radius)):
        #     ans.append(min(radius[i]))
        # print(ans)
        # return max(ans)
    

    

        
        # def checker(mid,house):
        #     if mid > house:
        #         r = mid - 1
        #     elif mid < house:
        #         l = mid + 1

        # l = 0
        # r = len(heaters)-1
        # while l <= r:
        #     mid = (l + r) // 2
        #     for house in houses:
        #         checker(mid , house)


            